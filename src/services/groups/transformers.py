from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.generated.all_groups import AllGroups
from src.generated.create_group import CreateGroup
from src.generated.fragments import GroupFields, UserInGroupFields
from src.generated.get_group import GetGroup
from src.generated.update_group import UpdateGroup

from src.exceptions import EetlijstException

from src.services.users.transformers import UserResult, transform_user


class GroupSummaryResult(BaseModel):
    payed_total: float
    user_id: str


class UserInGroupResult(BaseModel):
    order: Optional[int] = None
    start_holliday: Optional[datetime] = None
    end_holliday: Optional[datetime] = None
    monday: Optional[bool] = None
    tuesday: Optional[bool] = None
    wednesday: Optional[bool] = None
    thursday: Optional[bool] = None
    friday: Optional[bool] = None
    saturday: Optional[bool] = None
    sunday: Optional[bool] = None
    user: Optional[UserResult] = None


class GroupResult(BaseModel):
    id: str
    name: str
    default_close_time: Optional[datetime]
    created_at: datetime
    created_at_eetlijst: Optional[datetime]
    statistics_start_date: Optional[datetime]
    statistics_end_date: Optional[datetime]
    invite_uuid: str
    invite_open: bool
    description: Optional[str]
    summary: list[GroupSummaryResult]
    users: list[UserInGroupResult] = []


def transform_group(
    group: Optional[GroupFields],
    users: Optional[list[UserInGroupResult]] = None,
) -> GroupResult:
    if not group:
        raise EetlijstException("Group not found")

    filtered_summary = [
        GroupSummaryResult(
            payed_total=float(entry.payed_total),
            user_id=entry.user_id,
        )
        for entry in (group.summary or [])
        if entry and entry.payed_total is not None and entry.user_id is not None
    ]

    group_data = group.model_dump(exclude={"summary"})
    return GroupResult(
        **group_data,
        summary=filtered_summary,
        users=users or [],
    )


def transform_user_in_group(
    user_in_group: Optional[UserInGroupFields],
) -> UserInGroupResult:
    if not user_in_group:
        raise EetlijstException("User in group not found")

    user_data = transform_user(user_in_group.user) if user_in_group.user else None
    data = user_in_group.model_dump(exclude={"user"})

    return UserInGroupResult(
        **data,
        user=user_data,
    )


def transform_create_group(result: CreateGroup) -> GroupResult:
    if not result.group:
        raise EetlijstException("Failed to create group")

    return transform_group(result.group)


def transform_update_group(result: UpdateGroup) -> GroupResult:
    if not result.group:
        raise EetlijstException("Failed to update group")

    return transform_group(result.group)


def transform_all_groups(
    result: AllGroups,
    include_users: bool = False,
) -> list[GroupResult]:
    transformed_groups: list[GroupResult] = []
    for user_in_group in result.eetschema_users_in_group:
        if not user_in_group.group:
            continue

        users = (
            [transform_user_in_group(u) for u in user_in_group.group.users_in_groups]
            if include_users and user_in_group.group.users_in_groups
            else []
        )

        transformed_groups.append(transform_group(user_in_group.group, users=users))

    return transformed_groups


def transform_get_group(
    result: GetGroup,
    include_users: bool = False,
) -> GroupResult:
    if not result.eetschema_group_by_pk:
        raise EetlijstException("Failed to get group")

    users = (
        [
            transform_user_in_group(u)
            for u in result.eetschema_group_by_pk.users_in_groups
        ]
        if include_users and result.eetschema_group_by_pk.users_in_groups
        else []
    )

    return transform_group(result.eetschema_group_by_pk, users=users)
