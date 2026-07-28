"""Group Users service type exports."""

from typing import Optional, TypedDict

from eetlijst_py.generated.all_users_in_group import (
    AllUsersInGroupEetschemaGroupByPkUsersInGroups,
)
from eetlijst_py.generated.fragments import UserInGroupFields, UserInGroupFieldsUser
from eetlijst_py.generated.get_user_in_group import (
    GetUserInGroupEetschemaGroupByPkUsersInGroups,
)
from eetlijst_py.generated.input_types import (
    eetschema_users_in_group_bool_exp as _eetschema_users_in_group_bool_exp,
)
from eetlijst_py.generated.input_types import (
    eetschema_users_in_group_order_by as _eetschema_users_in_group_order_by,
)
from eetlijst_py.generated.input_types import (
    eetschema_users_in_group_set_input as _eetschema_users_in_group_set_input,
)
from eetlijst_py.generated.input_types import (
    eetschema_users_in_group_updates as _eetschema_users_in_group_updates,
)
from eetlijst_py.generated.update_user_in_group import (
    UpdateUserInGroupUpdateEetschemaUsersInGroupByPk,
)
from eetlijst_py.generated.update_users_in_group import (
    UpdateUsersInGroupUpdateEetschemaUsersInGroupManyUsersInGroup,
)

from eetlijst_py.services.groups.types import UserInGroup


class JoinedGroup(TypedDict):
    accepted: bool
    error: Optional[str]


class UpdatedUsersInGroup(TypedDict):
    number_users_in_group: int
    users_in_group: list[UserInGroup]


WhereUserInGroup = _eetschema_users_in_group_bool_exp
OrderUserInGroup = _eetschema_users_in_group_order_by
UpdateUserInGroup = _eetschema_users_in_group_set_input
UpdateUsersInGroup = _eetschema_users_in_group_updates

__all__ = [
    "JoinedGroup",
    "UpdatedUsersInGroup",
    "UserInGroupFields",
    "UserInGroupFieldsUser",
    "AllUsersInGroupEetschemaGroupByPkUsersInGroups",
    "GetUserInGroupEetschemaGroupByPkUsersInGroups",
    "UpdateUserInGroupUpdateEetschemaUsersInGroupByPk",
    "UpdateUsersInGroupUpdateEetschemaUsersInGroupManyUsersInGroup",
    "WhereUserInGroup",
    "OrderUserInGroup",
    "UpdateUserInGroup",
    "UpdateUsersInGroup",
]
