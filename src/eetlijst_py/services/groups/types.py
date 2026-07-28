"""Groups service type exports."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from eetlijst_py.generated.all_groups import (
    AllGroupsEetschemaGroupUsersInGroups,
)
from eetlijst_py.generated.create_group import CreateGroupGroup
from eetlijst_py.generated.fragments import (
    GroupFields,
    GroupFieldsSummary,
)
from eetlijst_py.generated.get_group import GetGroupEetschemaGroupByPk
from eetlijst_py.generated.input_types import (
    eetschema_group_bool_exp as _eetschema_group_bool_exp,
)
from eetlijst_py.generated.input_types import (
    eetschema_group_order_by as _eetschema_group_order_by,
)
from eetlijst_py.generated.input_types import (
    eetschema_group_set_input as _eetschema_group_set_input,
)
from eetlijst_py.generated.join_group import JoinGroupJoinGroup
from eetlijst_py.generated.update_group import UpdateGroupGroup

from eetlijst_py.services.event_attendance.types import AttendanceStatus
from eetlijst_py.services.users.types import User


class GroupSummary(BaseModel):
    payed_total: float
    user_id: str


class UserInGroup(BaseModel):
    active: bool
    order: Optional[int]
    start_holliday: Optional[datetime]
    end_holliday: Optional[datetime]
    monday: Optional[AttendanceStatus]
    tuesday: Optional[AttendanceStatus]
    wednesday: Optional[AttendanceStatus]
    thursday: Optional[AttendanceStatus]
    friday: Optional[AttendanceStatus]
    saturday: Optional[AttendanceStatus]
    sunday: Optional[AttendanceStatus]
    user: User


class Group(BaseModel):
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
    summary: list[GroupSummary]
    users: list[UserInGroup]


OrderGroup = _eetschema_group_order_by
UpdateGroup = _eetschema_group_set_input
WhereGroup = _eetschema_group_bool_exp

__all__ = [
    "Group",
    "GroupSummary",
    "UserInGroup",
    "GroupFields",
    "GroupFieldsSummary",
    "AllGroupsEetschemaGroupUsersInGroups",
    "GetGroupEetschemaGroupByPk",
    "CreateGroupGroup",
    "UpdateGroupGroup",
    "JoinGroupJoinGroup",
    "OrderGroup",
    "UpdateGroup",
    "WhereGroup",
]
