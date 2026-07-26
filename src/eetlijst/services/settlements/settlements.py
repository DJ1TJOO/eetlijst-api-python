import asyncio
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List, Optional, TypedDict

from eetlijst.generated import GraphQlClient, order_by
from eetlijst.generated.fragments import ExpenseFields
from eetlijst.generated.input_types import (
    Boolean_comparison_exp,
    eetschema_expense_bool_exp,
    eetschema_expense_distribution_insert_input,
    eetschema_expense_order_by,
    eetschema_expense_set_input,
    eetschema_settlements_bool_exp,
    eetschema_settlements_order_by,
    uuid_comparison_exp,
)
from eetlijst.services.expenses.transformers import (
    transform_create_expense,
    transform_update_expense,
)
from eetlijst.services.expenses.utils import calculate_balances_from_expenses
from eetlijst.services.settlements.transformers import (
    SettlementResult,
    transform_create_settlement,
    transform_settle_unsettled_expenses,
    transform_settlement,
    transform_settlement_expenses,
)
from eetlijst.services.settlements.utils import (
    CalculatedAdjustmentExpense,
    calculate_adjustment_expenses,
)


class SettleResult(TypedDict):
    id: str
    expenses: list[ExpenseFields]
    adjustments: list[ExpenseFields]


@dataclass
class Settlements:
    _client: GraphQlClient

    async def get(self, settlement_id: str) -> Optional[SettlementResult]:
        result = await self._client.all_settlements(
            where=eetschema_settlements_bool_exp(
                id=uuid_comparison_exp(_eq=settlement_id)
            )
        )

        return transform_settlement(result.eetschema_settlements[0])

    async def all(
        self,
        group_id: str,
        where: Optional[eetschema_settlements_bool_exp] = None,
        order: Optional[list[eetschema_settlements_order_by]] = None,
        limit: Optional[int] = None,
    ) -> list[SettlementResult]:
        group_filter = uuid_comparison_exp(_eq=group_id)
        where_data = (
            where.model_copy(update={"group_id": group_filter})
            if where is not None
            else eetschema_settlements_bool_exp(group_id=group_filter)
        )

        order_data = order or [eetschema_settlements_order_by(created_at=order_by.desc)]

        result = await self._client.all_settlements(
            where=where_data,
            order=order_data,
            limit=limit,
        )
        return [transform_settlement(s) for s in result.eetschema_settlements]

    async def create(self, group_id: str) -> SettlementResult:
        result = await self._client.create_settlement(group_id=group_id)
        return transform_create_settlement(result)

    async def settle(
        self,
        group_id: str,
        settlement_id: Optional[str] = None,
        do_not_create_adjustment_expenses: bool = False,
        select: Optional[eetschema_expense_bool_exp] = None,
    ) -> SettleResult:
        if settlement_id is None:
            settlement = await self.create(group_id=group_id)
            settlement_id = settlement.id

        group_filter = uuid_comparison_exp(_eq=group_id)
        settled_filter = uuid_comparison_exp(_is_null=True)

        if select is not None:
            where_data = select.model_copy(
                update={
                    "group_id": group_filter,
                    "settled_id": settled_filter,
                }
            )
        else:
            where_data = eetschema_expense_bool_exp(
                group_id=group_filter,
                settled_id=settled_filter,
            )

        result = await self._client.settle_unsettled_expenses(
            settlement_id=settlement_id,
            where=where_data,
        )
        settled = transform_settle_unsettled_expenses(result)

        inserted_adjustments: List[ExpenseFields] = []
        if not do_not_create_adjustment_expenses:
            balances = calculate_balances_from_expenses(settled.expenses)
            adjustments = calculate_adjustment_expenses(balances)

            now = datetime.now(timezone.utc)
            description = f"Vereffening {now.strftime('%d-%m-%Y')}"

            async def create_and_update_adjustment(
                adjustment: CalculatedAdjustmentExpense,
            ) -> ExpenseFields:
                distribution_data = [
                    eetschema_expense_distribution_insert_input(
                        user_id=d["user"].id,
                        payed_amount=d["payed_amount"],
                        count=d["count"],
                    )
                    for d in adjustment["expense_distributions"]
                ]

                created_raw = await self._client.create_expense(
                    group_id=group_id,
                    payed_by=adjustment["payed_by"].id,
                    payed_amount=adjustment["payed_amount"],
                    payed_at=now,
                    description=description,
                    settlement_expense_id=settlement_id,
                    data=distribution_data,
                )
                created_expense = transform_create_expense(created_raw)

                updated_raw = await self._client.update_expense(
                    expense_id=created_expense.id,
                    set_=eetschema_expense_set_input(settled_id=settlement_id),
                )
                return transform_update_expense(updated_raw)

            inserted_adjustments = list(
                await asyncio.gather(
                    *(create_and_update_adjustment(adj) for adj in adjustments)
                )
            )

        return {
            "id": settlement_id,
            "expenses": settled.expenses,
            "adjustments": inserted_adjustments,
        }

    async def expenses(
        self,
        settlement_id: str,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
    ) -> list[ExpenseFields]:
        return await self._expenses(
            settlement_id=settlement_id,
            settlement_expense_id_not_null=False,
            where=where,
            order=order,
        )

    async def adjustments(
        self,
        settlement_id: str,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
    ) -> list[ExpenseFields]:
        return await self._expenses(
            settlement_id=settlement_id,
            settlement_expense_id_not_null=True,
            where=where,
            order=order,
        )

    async def _expenses(
        self,
        settlement_id: str,
        settlement_expense_id_not_null: bool,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
    ) -> list[ExpenseFields]:
        deleted_filter = Boolean_comparison_exp(_eq=False)
        settled_filter = uuid_comparison_exp(_eq=settlement_id)
        settlement_expense_filter = uuid_comparison_exp(
            _is_null=not settlement_expense_id_not_null
        )

        if where is not None:
            where_data = where.model_copy(
                update={
                    "deleted": deleted_filter,
                    "settled_id": settled_filter,
                    "settlement_expense_id": settlement_expense_filter,
                }
            )
        else:
            where_data = eetschema_expense_bool_exp(
                deleted=deleted_filter,
                settled_id=settled_filter,
                settlement_expense_id=settlement_expense_filter,
            )

        order_data = order or [eetschema_expense_order_by(created_at=order_by.desc)]

        result = await self._client.settlement_expenses(
            where=where_data,
            order=order_data,
        )
        return transform_settlement_expenses(result)
