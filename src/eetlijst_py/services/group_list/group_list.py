from dataclasses import dataclass
from typing import Optional

from eetlijst_py.generated.input_types import (
    uuid_comparison_exp,
)

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.base import BaseService
from eetlijst_py.services.group_list.transformers import (
    transform_create_list_item,
    transform_create_many_list_items,
    transform_list_item,
    transform_update_list_item,
)
from eetlijst_py.services.group_list.types import (
    CreateListItem,
    OrderListItem,
    UpdateListItem,
    WhereListItem,
)

from eetlijst_py.utils.params import build_where


@dataclass
class GroupList(BaseService):

    async def get(self, item_id: str):
        result = await self._client.get_list_item(
            id=item_id,
            headers=self._get_headers(),
        )

        return transform_list_item(result.eetschema_list_by_pk)

    async def get_subscription(self, item_id: str):
        async for result in self._client.get_list_item_subscription(
            id=item_id,
            additional_headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_list_by_pk:
                yield transform_list_item(result.eetschema_list_by_pk)

    async def items(
        self,
        group_id: str,
        where: Optional[WhereListItem] = None,
        order: Optional[list[OrderListItem]] = None,
        limit: Optional[int] = None,
    ):
        where_data = build_where(
            WhereListItem,
            where,
            group_id=uuid_comparison_exp(_eq=group_id),
        )

        result = await self._client.list_items(
            where=where_data,
            order=order,
            limit=limit,
            headers=self._get_headers(),
        )

        return [transform_list_item(item) for item in result.eetschema_list]

    async def items_subscription(
        self,
        group_id: str,
        where: Optional[WhereListItem] = None,
        order: Optional[list[OrderListItem]] = None,
        limit: Optional[int] = None,
    ):
        where_data = build_where(
            WhereListItem,
            where,
            group_id=uuid_comparison_exp(_eq=group_id),
        )

        async for result in self._client.list_items_subscription(
            where=where_data,
            order=order,
            limit=limit,
            additional_headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_list:
                yield [transform_list_item(item) for item in result.eetschema_list]

    async def create_item(self, data: CreateListItem):
        result = await self._client.create_list_item(*data, headers=self._get_headers())
        return transform_create_list_item(result)

    async def create_many_items(self, items: list[CreateListItem]):
        result = await self._client.create_many_list_items(
            items=items,
            headers=self._get_headers(),
        )
        return transform_create_many_list_items(result)

    async def update_item(self, item_id: str, data: UpdateListItem):
        result = await self._client.update_list_item(
            id=item_id,
            set_=data,
            headers=self._get_headers(),
        )
        return transform_update_list_item(result)

    async def toggle_item(self, item_id: str):
        item = await self.get(item_id)
        if not item:
            raise EetlijstException("List item not found")

        return await self.update_item(
            item_id=item_id,
            data=UpdateListItem(checked=not item.checked),
        )

    async def check_item(self, item_id: str, state: bool = True):
        return await self.update_item(
            item_id=item_id,
            data=UpdateListItem(checked=state),
        )

    async def remove_item(self, item_id: str):
        return await self.update_item(
            item_id=item_id,
            data=UpdateListItem(active=False),
        )
