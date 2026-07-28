from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

from eetlijst_py.generated import order_by
from eetlijst_py.generated.input_types import (
    String_comparison_exp,
    eetschema_group_order_by,
    eetschema_group_set_input,
    eetschema_users_in_group_bool_exp,
    eetschema_users_in_group_order_by,
)

from eetlijst_py.services.base import BaseService
from eetlijst_py.services.group_list import GroupList
from eetlijst_py.services.groups.transformers import (
    GroupResult,
    transform_all_groups,
    transform_create_group,
    transform_get_group,
    transform_update_group,
)

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
    ) -> GroupResult:
        result = await self._client.get_group(
            group_id=group_id,
            include_users=include_users,
            include_inactive_users=include_inactive_users,
            headers=self._get_headers(),
        )
        return transform_get_group(result)

    async def all(
        self,
        user_id: str,
        include_users: bool = False,
        include_inactive_users: bool = False,
        where: Optional[eetschema_users_in_group_bool_exp] = None,
        order: Optional[List[eetschema_users_in_group_order_by]] = None,
        limit: Optional[int] = None,
    ) -> List[GroupResult]:
        where_data = (
            where.model_copy(update={"user_id": String_comparison_exp(_eq=user_id)})
            if where is not None
            else eetschema_users_in_group_bool_exp(
                user_id=String_comparison_exp(_eq=user_id)
            )
        )

        order_data = order or [
            eetschema_users_in_group_order_by(
                group=eetschema_group_order_by(created_at=order_by.asc)
            )
        ]

        result = await self._client.all_groups(
            where=where_data,
            order=order_data,
            limit=limit,
            include_users=include_users,
            include_inactive_users=include_inactive_users,
            headers=self._get_headers(),
        )

        return transform_all_groups(result)

    async def create(self, name: str, user_id: str) -> GroupResult:
        result = await self._client.create_group(
            name=name,
            user_id=user_id,
            headers=self._get_headers(),
        )
        return transform_create_group(result)

    async def update(
        self, group_id: str, data: eetschema_group_set_input
    ) -> GroupResult:
        result = await self._client.update_group(
            group_id=group_id,
            set_=data,
            headers=self._get_headers(),
        )
        return transform_update_group(result)
