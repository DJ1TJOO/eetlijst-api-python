from dataclasses import dataclass
from typing import Optional

from eetlijst_py.generated.input_types import (
    eetschema_list_bool_exp,
    eetschema_list_insert_input,
    eetschema_list_order_by,
    eetschema_list_set_input,
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


@dataclass
class GroupList(BaseService):

    async def get(self, item_id: str):
        result = await self._client.list_items(
            where=eetschema_list_bool_exp(id=uuid_comparison_exp(_eq=item_id)),
            headers=self._get_headers(),
        )

        return transform_list_item(result.eetschema_list[0])

    async def items(
        self,
        group_id: str,
        where: Optional[eetschema_list_bool_exp] = None,
        order: Optional[list[eetschema_list_order_by]] = None,
        limit: Optional[int] = None,
    ):
        if where is not None:
            where_data = where.model_copy(
                update={
                    "group_id": uuid_comparison_exp(_eq=group_id),
                }
            )
        else:
            where_data = eetschema_list_bool_exp(
                group_id=uuid_comparison_exp(_eq=group_id),
            )

        result = await self._client.list_items(
            where=where_data,
            order=order,
            limit=limit,
            headers=self._get_headers(),
        )

        return [transform_list_item(item) for item in result.eetschema_list]

    async def create_item(self, data: eetschema_list_insert_input):
        result = await self._client.create_list_item(*data, headers=self._get_headers())
        return transform_create_list_item(result)

    async def create_many_items(self, items: list[eetschema_list_insert_input]):
        result = await self._client.create_many_list_items(
            items=items,
            headers=self._get_headers(),
            headers=self._get_headers(),
        )
        return transform_create_many_list_items(result)

    async def update_item(self, item_id: str, data: eetschema_list_set_input):
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
            data=eetschema_list_set_input(checked=not item.checked),
        )

    async def check_item(self, item_id: str, state: bool = True):
        return await self.update_item(
            item_id=item_id,
            data=eetschema_list_set_input(checked=state),
        )

    async def remove_item(self, item_id: str):
        return await self.update_item(
            item_id=item_id,
            data=eetschema_list_set_input(active=False),
        )
