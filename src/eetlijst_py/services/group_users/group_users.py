from dataclasses import dataclass
from typing import Optional, TypedDict, Union

from eetlijst_py.generated import order_by
from eetlijst_py.generated.input_types import (
    Boolean_comparison_exp,
    String_comparison_exp,
    eetschema_users_in_group_bool_exp,
    eetschema_users_in_group_order_by,
    eetschema_users_in_group_set_input,
    eetschema_users_in_group_updates,
    uuid_comparison_exp,
)

from eetlijst_py.services.base import BaseService
from eetlijst_py.services.group_users.transformers import (
    transform_all_users_in_group,
    transform_get_user_in_group,
    transform_join_group,
    transform_update_user_in_group,
    transform_update_users_in_group,
)


class UserOrderItem(TypedDict):
    user_id: str
    order: int


@dataclass
class GroupUsers(BaseService):

    async def get(self, group_id: str, user_id: str):
        result = await self._client.get_user_in_group(
            group_id=group_id,
            user_id=user_id,
            headers=self._get_headers(),
        )
        return transform_get_user_in_group(result)

    async def all(
        self,
        group_id: str,
        include_inactive_users: bool = False,
        where: Optional[eetschema_users_in_group_bool_exp] = None,
        order: Optional[list[eetschema_users_in_group_order_by]] = None,
        limit: Optional[int] = None,
    ):
        if where is not None:
            update_data: dict[
                str, Union[uuid_comparison_exp, Boolean_comparison_exp]
            ] = {"group_id": uuid_comparison_exp(_eq=group_id)}
            if not include_inactive_users:
                update_data["active"] = Boolean_comparison_exp(_eq=True)

            where_data = where.model_copy(update=update_data)
        else:
            where_data = eetschema_users_in_group_bool_exp(
                group_id=uuid_comparison_exp(_eq=group_id),
                active=(
                    None if include_inactive_users else Boolean_comparison_exp(_eq=True)
                ),
            )

        order_data = order or [eetschema_users_in_group_order_by(order=order_by.asc)]

        result = await self._client.all_users_in_group(
            group_id=group_id,
            where=where_data,
            order=order_data,
            limit=limit,
            headers=self._get_headers(),
        )

        return transform_all_users_in_group(result)

    async def add(self, group_id: str, user_id: str, invite_id: str):
        result = await self._client.join_group(
            group_id,
            user_id,
            invite_id,
            headers=self._get_headers(),
            headers=self._get_headers(),
        )
        return transform_join_group(result)

    async def update(
        self,
        group_id: str,
        user_id: str,
        data: eetschema_users_in_group_set_input,
    ):
        result = await self._client.update_user_in_group(
            group_id=group_id,
            user_id=user_id,
            set_=data,
            headers=self._get_headers(),
        )

        return transform_update_user_in_group(result)

    async def update_many(
        self,
        updates: list[eetschema_users_in_group_updates],
    ):
        result = await self._client.update_users_in_group(
            updates=updates,
            headers=self._get_headers(),
            headers=self._get_headers(),
        )
        return transform_update_users_in_group(result)

    async def remove(self, group_id: str, user_id: str):
        return await self.update(
            group_id=group_id,
            user_id=user_id,
            data=eetschema_users_in_group_set_input(active=False),
        )

    async def order(
        self,
        group_id: str,
        user_order: list[Union[str, UserOrderItem]],
        offset: int = 0,
    ):
        updates: list[eetschema_users_in_group_updates] = []

        for index, item in enumerate(user_order):
            if isinstance(item, str):
                target_user_id = item
                target_order = index + offset
            else:
                target_user_id = item["user_id"]
                target_order = item["order"] + offset

            updates.append(
                eetschema_users_in_group_updates(
                    where=eetschema_users_in_group_bool_exp(
                        group_id=uuid_comparison_exp(_eq=group_id),
                        user_id=String_comparison_exp(_eq=target_user_id),
                    ),
                    _set=eetschema_users_in_group_set_input(order=target_order),
                )
            )

        return await self.update_many(updates)
