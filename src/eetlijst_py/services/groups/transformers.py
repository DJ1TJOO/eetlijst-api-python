from typing import Optional, Sequence

from eetlijst_py.generated.all_groups import AllGroups
from eetlijst_py.generated.all_groups_subscription import AllGroupsSubscription
from eetlijst_py.generated.create_group import CreateGroup
from eetlijst_py.generated.fragments import GroupFields, UserInGroupFields
from eetlijst_py.generated.get_group import GetGroup
from eetlijst_py.generated.get_group_subscription import GetGroupSubscription
from eetlijst_py.generated.update_group import UpdateGroup

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.groups.types import (
    Group,
    GroupSummary,
    UserInGroup,
)
from eetlijst_py.services.users.transformers import transform_user


def transform_group(
    group: Optional[GroupFields],
    users: Optional[list[UserInGroup]] = None,
) -> Group:
    if not group:
        raise EetlijstException("Group not found")

    filtered_summary = [
        GroupSummary(
            payed_total=float(entry.payed_total),
            user_id=entry.user_id,
        )
        for entry in (group.summary or [])
        if entry and entry.payed_total is not None and entry.user_id is not None
    ]

    group_data = group.model_dump(exclude={"summary"})
    return Group(
        **group_data,
        summary=filtered_summary,
        users=users or [],
    )


def transform_user_in_group(
    user_in_group: Optional[UserInGroupFields],
) -> UserInGroup:
    if not user_in_group:
        raise EetlijstException("User in group not found")

    user_data = transform_user(user_in_group.user)
    data = user_in_group.model_dump(exclude={"user"})

    return UserInGroup(
        **data,
        user=user_data,
    )


def transform_create_group(result: CreateGroup) -> Group:
    if not result.group:
        raise EetlijstException("Failed to create group")

    return transform_group(result.group)


def transform_update_group(result: UpdateGroup) -> Group:
    if not result.group:
        raise EetlijstException("Failed to update group")

    return transform_group(result.group)


def transform_users_in_group(
    users_in_groups: Sequence[UserInGroupFields] | None,
) -> list[UserInGroup]:
    if not users_in_groups:
        return []

    return [transform_user_in_group(user) for user in users_in_groups]


def transform_all_groups(
    result: AllGroups | AllGroupsSubscription,
) -> list[Group]:
    return [
        transform_group(group, users=transform_users_in_group(group.users_in_groups))
        for group in result.eetschema_group
    ]


def transform_get_group(
    result: GetGroup | GetGroupSubscription,
) -> Group:
    if not result.eetschema_group_by_pk:
        raise EetlijstException("Failed to get group")

    group = result.eetschema_group_by_pk
    return transform_group(group, users=transform_users_in_group(group.users_in_groups))
