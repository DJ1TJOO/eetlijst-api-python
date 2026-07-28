import asyncio
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import AsyncIterator, List, Optional, TypedDict

from eetlijst_py.generated import order_by
from eetlijst_py.generated.fragments import ExpenseFields
from eetlijst_py.generated.input_types import (
    Boolean_comparison_exp,
    eetschema_expense_bool_exp,
    eetschema_expense_distribution_insert_input,
    eetschema_expense_order_by,
    eetschema_expense_set_input,
    eetschema_settlements_bool_exp,
    eetschema_settlements_order_by,
    uuid_comparison_exp,
)

from eetlijst_py.services.base import BaseService
from eetlijst_py.services.expenses.transformers import (
    transform_create_expense,
    transform_update_expense,
)
from eetlijst_py.services.expenses.utils import calculate_balances_from_expenses
from eetlijst_py.services.settlements.transformers import (
    SettlementResult,
    transform_create_settlement,
    transform_settle_unsettled_expenses,
    transform_settlement,
    transform_settlement_expenses,
)
from eetlijst_py.services.settlements.utils import (
    CalculatedAdjustmentExpense,
    calculate_adjustment_expenses,
)

from eetlijst_py.utils.params import build_where, default_order


class SettleResult(TypedDict):
    id: str
    expenses: list[ExpenseFields]
    adjustments: list[ExpenseFields]


@dataclass
class Settlements(BaseService):

    async def get(self, settlement_id: str) -> SettlementResult | None:
        result = await self._client.get_settlement(
            id=settlement_id,
            headers=self._get_headers(),
        )

        return transform_settlement(result.eetschema_settlements_by_pk)

    async def get_subscription(
        self, settlement_id: str
    ) -> AsyncIterator[SettlementResult]:
        async for result in self._client.get_settlement_subscription(
            id=settlement_id,
            headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_settlements_by_pk:
                yield transform_settlement(result.eetschema_settlements_by_pk)

    async def all(
        self,
        group_id: str,
        where: Optional[eetschema_settlements_bool_exp] = None,
        order: Optional[list[eetschema_settlements_order_by]] = None,
        limit: Optional[int] = None,
    ) -> list[SettlementResult]:
        where_data = build_where(
            eetschema_settlements_bool_exp,
            where,
            group_id=uuid_comparison_exp(_eq=group_id),
        )

        order_data = default_order(
            order,
            eetschema_settlements_order_by(created_at=order_by.asc),
        )

        result = await self._client.all_settlements(
            where=where_data,
            order=order_data,
            limit=limit,
            headers=self._get_headers(),
        )
        return [transform_settlement(s) for s in result.eetschema_settlements]

    async def all_subscription(
        self,
        group_id: str,
        where: Optional[eetschema_settlements_bool_exp] = None,
        order: Optional[list[eetschema_settlements_order_by]] = None,
        limit: Optional[int] = None,
    ):
        where_data = build_where(
            eetschema_settlements_bool_exp,
            where,
            group_id=uuid_comparison_exp(_eq=group_id),
        )

        order_data = default_order(
            order,
            eetschema_settlements_order_by(created_at=order_by.asc),
        )

        async for result in self._client.all_settlements_subscription(
            where=where_data,
            order=order_data,
            limit=limit,
            headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_settlements:
                yield [transform_settlement(s) for s in result.eetschema_settlements]

    async def create(self, group_id: str) -> SettlementResult:
        result = await self._client.create_settlement(
            group_id=group_id,
            headers=self._get_headers(),
        )
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

        where_data = build_where(
            eetschema_expense_bool_exp,
            select,
            group_id=uuid_comparison_exp(_eq=group_id),
            settled_id=uuid_comparison_exp(_is_null=True),
        )

        result = await self._client.settle_unsettled_expenses(
            settlement_id=settlement_id,
            where=where_data,
            headers=self._get_headers(),
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
                    headers=self._get_headers(),
                )
                created_expense = transform_create_expense(created_raw)

                updated_raw = await self._client.update_expense(
                    expense_id=created_expense.id,
                    set_=eetschema_expense_set_input(settled_id=settlement_id),
                    headers=self._get_headers(),
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
        limit: Optional[int] = None,
    ) -> list[ExpenseFields]:
        return await self._expenses(
            settlement_id=settlement_id,
            settlement_expense_id_not_null=False,
            where=where,
            order=order,
            limit=limit,
        )

    async def adjustments(
        self,
        settlement_id: str,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
        limit: Optional[int] = None,
    ) -> list[ExpenseFields]:
        return await self._expenses(
            settlement_id=settlement_id,
            settlement_expense_id_not_null=True,
            where=where,
            order=order,
            limit=limit,
        )

    async def _expenses(
        self,
        settlement_id: str,
        settlement_expense_id_not_null: bool,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
        limit: Optional[int] = None,
    ) -> list[ExpenseFields]:
        where_data = build_where(
            eetschema_expense_bool_exp,
            where,
            deleted=Boolean_comparison_exp(_eq=False),
            settled_id=uuid_comparison_exp(_eq=settlement_id),
            settlement_expense_id=uuid_comparison_exp(
                _is_null=not settlement_expense_id_not_null
            ),
        )

        order_data = default_order(
            order,
            eetschema_expense_order_by(created_at=order_by.asc),
        )

        result = await self._client.settlement_expenses(
            where=where_data,
            order=order_data,
            limit=limit,
            headers=self._get_headers(),
        )
        return transform_settlement_expenses(result)

    async def expenses_subscription(
        self,
        settlement_id: str,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
        limit: Optional[int] = None,
    ) -> AsyncIterator[list[ExpenseFields]]:
        async for items in self._expenses_subscription(
            settlement_id=settlement_id,
            settlement_expense_id_not_null=False,
            where=where,
            order=order,
            limit=limit,
        ):
            yield items

    async def adjustments_subscription(
        self,
        settlement_id: str,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
        limit: Optional[int] = None,
    ) -> AsyncIterator[list[ExpenseFields]]:
        async for items in self._expenses_subscription(
            settlement_id=settlement_id,
            settlement_expense_id_not_null=True,
            where=where,
            order=order,
            limit=limit,
        ):
            yield items

    async def _expenses_subscription(
        self,
        settlement_id: str,
        settlement_expense_id_not_null: bool,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
        limit: Optional[int] = None,
    ) -> AsyncIterator[list[ExpenseFields]]:
        where_data = build_where(
            eetschema_expense_bool_exp,
            where,
            deleted=Boolean_comparison_exp(_eq=False),
            settled_id=uuid_comparison_exp(_eq=settlement_id),
            settlement_expense_id=uuid_comparison_exp(
                _is_null=not settlement_expense_id_not_null
            ),
        )

        order_data = default_order(
            order,
            eetschema_expense_order_by(created_at=order_by.asc),
        )

        async for result in self._client.settlement_expenses_subscription(
            where=where_data,
            order=order_data,
            limit=limit,
            headers=self._get_ws_headers(),
        ):
            if result:
                yield transform_settlement_expenses(result)
