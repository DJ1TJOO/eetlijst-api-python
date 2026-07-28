from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

from eetlijst_py.generated import order_by
from eetlijst_py.generated.input_types import (
    String_comparison_exp,
)

from eetlijst_py.services.base import BaseService
from eetlijst_py.services.group_list import GroupList
from eetlijst_py.services.groups.transformers import (
    transform_all_groups,
    transform_create_group,
    transform_get_group,
    transform_update_group,
)
from eetlijst_py.services.groups.types import (
    OrderGroup,
    UpdateGroup,
    WhereGroup,
)

from eetlijst_py.utils.params import build_where, default_order

if TYPE_CHECKING:
    from eetlijst_py.services.group_users import GroupUsers


@dataclass
class Groups(BaseService):
    users: GroupUsers
    list: GroupList

    async def get(
        self,
        group_id: str,
        include_users: bool = False,
        include_inactive_users: bool = False,
    ):
        result = await self._client.get_group(
            group_id=group_id,
            include_users=include_users,
            include_inactive_users=include_inactive_users,
            headers=self._get_headers(),
        )

        return transform_get_group(result)

    async def get_subscription(
        self,
        group_id: str,
        include_users: bool = False,
        include_inactive_users: bool = False,
    ):
        async for result in self._client.get_group_subscription(
            group_id=group_id,
            include_users=include_users,
            include_inactive_users=include_inactive_users,
            additional_headers=self._get_ws_headers(),
        ):
            if result:
                yield transform_get_group(result)

    async def all(
        self,
        user_id: str,
        include_users: bool = False,
        include_inactive_users: bool = False,
        where: Optional[WhereGroup] = None,
        order: Optional[List[OrderGroup]] = None,
        limit: Optional[int] = None,
    ):
        where_data = build_where(
            WhereGroup,
            where,
            user_id=String_comparison_exp(_eq=user_id),
        )
        order_data = default_order(
            order,
            OrderGroup(created_at=order_by.asc),
        )

        result = await self._client.all_groups(
            where=where_data,
            order=order_data,
            limit=limit,
            include_users=include_users,
            include_inactive_users=include_inactive_users,
            headers=self._get_headers(),
        )

        return transform_all_groups(result)

    async def all_subscription(
        self,
        user_id: str,
        include_users: bool = False,
        include_inactive_users: bool = False,
        where: Optional[WhereGroup] = None,
        order: Optional[List[OrderGroup]] = None,
        limit: Optional[int] = None,
    ):
        where_data = build_where(
            WhereGroup,
            where,
            user_id=String_comparison_exp(_eq=user_id),
        )
        order_data = default_order(
            order,
            OrderGroup(created_at=order_by.asc),
        )

        async for result in self._client.all_groups_subscription(
            where=where_data,
            order=order_data,
            limit=limit,
            include_users=include_users,
            include_inactive_users=include_inactive_users,
            additional_headers=self._get_ws_headers(),
        ):
            if result:
                yield transform_all_groups(result)

    async def create(self, name: str, user_id: str):
        result = await self._client.create_group(
            name=name,
            user_id=user_id,
            headers=self._get_headers(),
        )
        return transform_create_group(result)

    async def update(self, group_id: str, data: UpdateGroup):
        result = await self._client.update_group(
            group_id=group_id,
            set_=data,
            headers=self._get_headers(),
        )
        return transform_update_group(result)
