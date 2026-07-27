from dataclasses import dataclass
from typing import Optional

from eetlijst_py.generated import GraphQlClient, order_by
from eetlijst_py.generated.input_types import (
    Boolean_comparison_exp,
    eetschema_expense_bool_exp,
    eetschema_expense_distribution_insert_input,
    eetschema_expense_insert_input,
    eetschema_expense_order_by,
    eetschema_expense_set_input,
    uuid_comparison_exp,
)

from eetlijst_py.services.expenses.transformers import (
    transform_create_expense,
    transform_expense,
    transform_group_total_expense,
    transform_update_expense,
)
from eetlijst_py.services.settlements import Settlements


@dataclass
class Expenses:
    _client: GraphQlClient
    settlements: Settlements

    async def get(self, expense_id: str):
        result = await self._client.all_expenses(
            where=eetschema_expense_bool_exp(id=uuid_comparison_exp(_eq=expense_id))
        )

        return transform_expense(result.eetschema_expense[0])

    async def all(
        self,
        group_id: str,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
        limit: Optional[int] = None,
    ):
        if where is not None:
            where_data = where.model_copy(
                update={
                    "deleted": Boolean_comparison_exp(_eq=False),
                    "group_id": uuid_comparison_exp(_eq=group_id),
                }
            )
        else:
            where_data = eetschema_expense_bool_exp(
                deleted=Boolean_comparison_exp(_eq=False),
                group_id=uuid_comparison_exp(_eq=group_id),
            )

        order_data = order
        if order_data is None:
            order_data = [eetschema_expense_order_by(created_at=order_by.asc)]

        result = await self._client.all_expenses(
            where=where_data,
            order=order_data,
            limit=limit,
        )

        return [transform_expense(expense) for expense in result.eetschema_expense]

    async def create(self, data: eetschema_expense_insert_input):
        result = await self._client.create_expense(*data)
        return transform_create_expense(result)

    async def update(self, expense_id: str, data: eetschema_expense_set_input):
        result = await self._client.update_expense(
            expense_id=expense_id,
            set_=data,
        )

        return transform_update_expense(result)

    async def update_distribution(
        self,
        expense_id: str,
        data: list[eetschema_expense_distribution_insert_input],
    ):
        await self._client.update_expense_distribution(
            expense_id=expense_id,
            objects=data,
        )

    async def delete(self, expense_id: str):
        return await self.update(
            expense_id=expense_id,
            data=eetschema_expense_set_input(deleted=True),
        )

    async def group_total(self, group_id: str):
        result = await self._client.group_total_expense(group_id=group_id)
        return transform_group_total_expense(result)
