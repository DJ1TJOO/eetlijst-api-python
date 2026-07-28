from asyncio import Queue, create_task
from dataclasses import dataclass
from typing import AsyncIterator, Optional

from eetlijst_py.generated import order_by
from eetlijst_py.generated.group_total_expense_import_subscription import (
    GroupTotalExpenseImportSubscription,
)
from eetlijst_py.generated.group_total_expense_subscription import (
    GroupTotalExpenseSubscription,
)
from eetlijst_py.generated.input_types import (
    Boolean_comparison_exp,
    eetschema_expense_bool_exp,
    eetschema_expense_distribution_insert_input,
    eetschema_expense_insert_input,
    eetschema_expense_order_by,
    eetschema_expense_set_input,
    uuid_comparison_exp,
)

from eetlijst_py.services.base import BaseService
from eetlijst_py.services.expenses.transformers import (
    transform_create_expense,
    transform_expense,
    transform_group_total_expense,
    transform_group_total_expense_subscription,
    transform_update_expense,
)
from eetlijst_py.services.settlements import Settlements

from eetlijst_py.utils.params import build_where, default_order


@dataclass
class Expenses(BaseService):
    settlements: Settlements

    async def get(self, expense_id: str):
        result = await self._client.get_expense(
            id=expense_id,
            headers=self._get_headers(),
        )

        return transform_expense(result.eetschema_expense_by_pk)

    async def get_subscription(self, expense_id: str):
        async for result in self._client.get_expense_subscription(
            id=expense_id,
            headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_expense_by_pk:
                yield transform_expense(result.eetschema_expense_by_pk)

    async def all(
        self,
        group_id: str,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
        limit: Optional[int] = None,
    ):
        where_data = build_where(
            eetschema_expense_bool_exp,
            where,
            deleted=Boolean_comparison_exp(_eq=False),
            group_id=uuid_comparison_exp(_eq=group_id),
        )
        order_data = default_order(
            order,
            eetschema_expense_order_by(created_at=order_by.asc),
        )

        result = await self._client.all_expenses(
            where=where_data,
            order=order_data,
            limit=limit,
            headers=self._get_headers(),
        )

        return [transform_expense(expense) for expense in result.eetschema_expense]

    async def all_subscription(
        self,
        group_id: str,
        where: Optional[eetschema_expense_bool_exp] = None,
        order: Optional[list[eetschema_expense_order_by]] = None,
        limit: Optional[int] = None,
    ):
        where_data = build_where(
            eetschema_expense_bool_exp,
            where,
            deleted=Boolean_comparison_exp(_eq=False),
            group_id=uuid_comparison_exp(_eq=group_id),
        )
        order_data = default_order(
            order,
            eetschema_expense_order_by(created_at=order_by.asc),
        )

        async for result in self._client.all_expenses_subscription(
            where=where_data,
            order=order_data,
            limit=limit,
            headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_expense:
                yield [
                    transform_expense(expense) for expense in result.eetschema_expense
                ]

    async def create(self, data: eetschema_expense_insert_input):
        result = await self._client.create_expense(*data, headers=self._get_headers())
        return transform_create_expense(result)

    async def update(self, expense_id: str, data: eetschema_expense_set_input):
        result = await self._client.update_expense(
            expense_id=expense_id,
            set_=data,
            headers=self._get_headers(),
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
            headers=self._get_headers(),
        )

    async def delete(self, expense_id: str):
        return await self.update(
            expense_id=expense_id,
            data=eetschema_expense_set_input(deleted=True),
        )

    async def group_total(self, group_id: str):
        result = await self._client.group_total_expense(
            group_id=group_id,
            headers=self._get_headers(),
        )
        return transform_group_total_expense(result)

    async def group_total_subscription(self, group_id: str):
        expense_subscription = self._client.group_total_expense_subscription(
            group_id=group_id, headers=self._get_ws_headers()
        )
        import_subscription = self._client.group_total_expense_import_subscription(
            group_id=group_id, headers=self._get_ws_headers()
        )

        type QueuePayload = (
            GroupTotalExpenseSubscription | GroupTotalExpenseImportSubscription
        )
        queue: Queue[QueuePayload] = Queue()

        async def listen(
            stream: AsyncIterator[QueuePayload],
        ):
            async for item in stream:
                if item is not None:
                    await queue.put(item)

        expense_task = create_task(listen(expense_subscription))
        import_task = create_task(listen(import_subscription))

        expenses: Optional[GroupTotalExpenseSubscription] = None
        imported: Optional[GroupTotalExpenseImportSubscription] = None

        try:
            while True:
                data = await queue.get()

                if isinstance(data, GroupTotalExpenseSubscription):
                    expenses = data
                elif isinstance(data, GroupTotalExpenseImportSubscription):
                    imported = data

                yield transform_group_total_expense_subscription(expenses, imported)
        finally:
            expense_task.cancel()
            import_task.cancel()
