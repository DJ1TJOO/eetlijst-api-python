from typing import Optional, TypedDict

from eetlijst_py.generated.all_users_in_group import AllUsersInGroup
from eetlijst_py.generated.all_users_in_group_subscription import (
    AllUsersInGroupSubscription,
)
from eetlijst_py.generated.get_user_in_group import GetUserInGroup
from eetlijst_py.generated.get_user_in_group_subscription import (
    GetUserInGroupSubscription,
)
from eetlijst_py.generated.join_group import JoinGroup
from eetlijst_py.generated.update_user_in_group import UpdateUserInGroup
from eetlijst_py.generated.update_users_in_group import UpdateUsersInGroup

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.groups.transformers import (
    UserInGroupResult,
    transform_user_in_group,
)


class JoinGroupResult(TypedDict):
    accepted: bool
    error: Optional[str]


class UpdateUsersInGroupResult(TypedDict):
    number_users_in_group: int
    users_in_group: list[UserInGroupResult]


def transform_join_group(result: JoinGroup) -> JoinGroupResult:
    if not result.join_group:
        raise EetlijstException("Failed to join group")

    return {
        "accepted": result.join_group.accepted,
        "error": result.join_group.error,
    }


def transform_update_users_in_group(
    result: UpdateUsersInGroup,
) -> UpdateUsersInGroupResult:
    if not result.update_eetschema_users_in_group_many:
        raise EetlijstException("Failed to update users in group")

    valid_results = [
        item for item in result.update_eetschema_users_in_group_many if item is not None
    ]

    updated_users_in_group = sum(item.number_users_in_group for item in valid_results)
    users_in_group = [
        transform_user_in_group(user)
        for item in valid_results
        for user in (item.users_in_group or [])
    ]

    return {
        "number_users_in_group": updated_users_in_group,
        "users_in_group": users_in_group,
    }


def transform_update_user_in_group(result: UpdateUserInGroup) -> UserInGroupResult:
    if not result.update_eetschema_users_in_group_by_pk:
        raise EetlijstException("Failed to update user in group")

    return transform_user_in_group(result.update_eetschema_users_in_group_by_pk)


def transform_all_users_in_group(
    result: AllUsersInGroup | AllUsersInGroupSubscription,
) -> list[UserInGroupResult]:
    if not result.eetschema_group_by_pk:
        raise EetlijstException("Failed to get users")

    return [
        transform_user_in_group(user)
        for user in result.eetschema_group_by_pk.users_in_groups
    ]


def transform_get_user_in_group(
    result: GetUserInGroup | GetUserInGroupSubscription,
) -> UserInGroupResult:
    if (
        not result.eetschema_group_by_pk
        or not result.eetschema_group_by_pk.users_in_groups
    ):
        raise EetlijstException("Failed to get user")

    return transform_user_in_group(result.eetschema_group_by_pk.users_in_groups[0])
