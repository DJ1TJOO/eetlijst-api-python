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
from eetlijst_py.generated.update_users_in_group import (
    UpdateUsersInGroup,
)

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.group_users.types import JoinedGroup, UpdatedUsersInGroup
from eetlijst_py.services.groups.transformers import (
    UserInGroup,
    transform_user_in_group,
)


def transform_join_group(result: JoinGroup) -> JoinedGroup:
    if not result.join_group:
        raise EetlijstException("Failed to join group")

    return {
        "accepted": result.join_group.accepted,
        "error": result.join_group.error,
    }


def transform_update_users_in_group(
    result: UpdateUsersInGroup,
) -> UpdatedUsersInGroup:
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


def transform_update_user_in_group(result: UpdateUserInGroup) -> UserInGroup:
    if not result.update_eetschema_users_in_group_by_pk:
        raise EetlijstException("Failed to update user in group")

    return transform_user_in_group(result.update_eetschema_users_in_group_by_pk)


def transform_all_users_in_group(
    result: AllUsersInGroup | AllUsersInGroupSubscription,
) -> list[UserInGroup]:
    if not result.eetschema_group_by_pk:
        raise EetlijstException("Failed to get users")

    return [
        transform_user_in_group(user)
        for user in result.eetschema_group_by_pk.users_in_groups
    ]


def transform_get_user_in_group(
    result: GetUserInGroup | GetUserInGroupSubscription,
) -> UserInGroup:
    if (
        not result.eetschema_group_by_pk
        or not result.eetschema_group_by_pk.users_in_groups
    ):
        raise EetlijstException("Failed to get user")

    return transform_user_in_group(result.eetschema_group_by_pk.users_in_groups[0])
