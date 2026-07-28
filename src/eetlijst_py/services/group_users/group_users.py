from dataclasses import dataclass
from typing import Optional, TypedDict, Union

from eetlijst_py.generated import order_by
from eetlijst_py.generated.input_types import (
    Boolean_comparison_exp,
    String_comparison_exp,
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
from eetlijst_py.services.group_users.types import (
    OrderUserInGroup,
    UpdateUserInGroup,
    UpdateUsersInGroup,
    WhereUserInGroup,
)

from eetlijst_py.utils.params import build_where, default_order


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

    async def get_subscription(self, group_id: str, user_id: str):
        async for result in self._client.get_user_in_group_subscription(
            group_id=group_id,
            user_id=user_id,
            headers=self._get_ws_headers(),
        ):
            if result:
                yield transform_get_user_in_group(result)

    async def all(
        self,
        group_id: str,
        include_inactive_users: bool = False,
        where: Optional[WhereUserInGroup] = None,
        order: Optional[list[OrderUserInGroup]] = None,
        limit: Optional[int] = None,
    ):
        where_data = build_where(
            WhereUserInGroup,
            where,
            group_id=uuid_comparison_exp(_eq=group_id),
            active=None if include_inactive_users else Boolean_comparison_exp(_eq=True),
        )

        order_data = default_order(
            order,
            OrderUserInGroup(order=order_by.asc),
        )

        result = await self._client.all_users_in_group(
            group_id=group_id,
            where=where_data,
            order=order_data,
            limit=limit,
            headers=self._get_headers(),
        )

        return transform_all_users_in_group(result)

    async def all_subscription(
        self,
        group_id: str,
        include_inactive_users: bool = False,
        where: Optional[WhereUserInGroup] = None,
        order: Optional[list[OrderUserInGroup]] = None,
        limit: Optional[int] = None,
    ):
        where_data = build_where(
            WhereUserInGroup,
            where,
            group_id=uuid_comparison_exp(_eq=group_id),
            active=None if include_inactive_users else Boolean_comparison_exp(_eq=True),
        )

        order_data = default_order(
            order,
            OrderUserInGroup(order=order_by.asc),
        )

        async for result in self._client.all_users_in_group_subscription(
            group_id=group_id,
            where=where_data,
            order=order_data,
            limit=limit,
            headers=self._get_ws_headers(),
        ):
            if result:
                yield transform_all_users_in_group(result)

    async def add(self, group_id: str, user_id: str, invite_id: str):
        result = await self._client.join_group(
            group_id,
            user_id,
            invite_id,
            headers=self._get_headers(),
        )
        return transform_join_group(result)

    async def update(
        self,
        group_id: str,
        user_id: str,
        data: UpdateUserInGroup,
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
        updates: list[UpdateUsersInGroup],
    ):
        result = await self._client.update_users_in_group(
            updates=updates,
            headers=self._get_headers(),
        )
        return transform_update_users_in_group(result)

    async def remove(self, group_id: str, user_id: str):
        return await self.update(
            group_id=group_id,
            user_id=user_id,
            data=UpdateUserInGroup(active=False),
        )

    async def order(
        self,
        group_id: str,
        user_order: list[Union[str, UserOrderItem]],
        offset: int = 0,
    ):
        updates: list[UpdateUsersInGroup] = []

        for index, item in enumerate(user_order):
            if isinstance(item, str):
                target_user_id = item
                target_order = index + offset
            else:
                target_user_id = item["user_id"]
                target_order = item["order"] + offset

            updates.append(
                UpdateUsersInGroup(
                    where=WhereUserInGroup(
                        group_id=uuid_comparison_exp(_eq=group_id),
                        user_id=String_comparison_exp(_eq=target_user_id),
                    ),
                    _set=UpdateUserInGroup(order=target_order),
                )
            )

        return await self.update_many(updates)
