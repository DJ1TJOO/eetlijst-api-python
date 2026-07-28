"""Event Attendance service type exports."""

from datetime import datetime
from enum import Enum
from typing import Optional

from eetlijst_py.generated.all_attendances import AllAttendancesEetschemaEventAttendees
from eetlijst_py.generated.base_model import BaseModel
from eetlijst_py.generated.fragments import (
    AttendanceFields,
    AttendanceFieldsLinkedEvent,
    AttendanceFieldsUserInGroup,
    AttendanceFieldsUserInGroupUser,
)
from eetlijst_py.generated.get_attendance import (
    GetAttendanceEetschemaEventAttendeesByPk,
)
from eetlijst_py.generated.input_types import (
    eetschema_event_attendees_bool_exp as _eetschema_event_attendees_bool_exp,
)
from eetlijst_py.generated.input_types import (
    eetschema_event_attendees_insert_input as _eetschema_event_attendees_insert_input,
)
from eetlijst_py.generated.input_types import (
    eetschema_event_attendees_order_by as _eetschema_event_attendees_order_by,
)
from eetlijst_py.generated.input_types import (
    eetschema_event_attendees_set_input as _eetschema_event_attendees_set_input,
)
from eetlijst_py.generated.update_attendance import (
    UpdateAttendanceUpdateEetschemaEventAttendeesByPk,
)
from eetlijst_py.generated.update_many_attendance import (
    UpdateManyAttendanceInsertEetschemaEventAttendeesReturning,
)


class AttendanceStatus(str, Enum):
    COOK = "cook"
    EAT_ONLY = "eat_only"
    GOT_GROCERIES = "got_groceries"
    NOT_ATTENDING = "not_attending"
    DONT_KNOW_YET = "dont_know_yet"


class Attendance(BaseModel):
    created_at: datetime
    updated_at: datetime
    comment: Optional[str]
    number_guests: int
    status: AttendanceStatus
    event: AttendanceFieldsLinkedEvent
    user: Optional[AttendanceFieldsUserInGroup]


class AttendEvent(_eetschema_event_attendees_insert_input):
    user_id: str
    event_id: str
    status: AttendanceStatus


class UpdateAttendance(_eetschema_event_attendees_set_input):
    user_id: str
    event_id: str


WhereEventAttendee = _eetschema_event_attendees_bool_exp
CreateEventAttendee = _eetschema_event_attendees_insert_input
OrderEventAttendee = _eetschema_event_attendees_order_by
UpdateEventAttendee = _eetschema_event_attendees_set_input

__all__ = [
    "AttendanceStatus",
    "Attendance",
    "AttendEvent",
    "UpdateAttendance",
    "AttendanceFields",
    "AttendanceFieldsLinkedEvent",
    "AttendanceFieldsUserInGroup",
    "AttendanceFieldsUserInGroupUser",
    "AllAttendancesEetschemaEventAttendees",
    "GetAttendanceEetschemaEventAttendeesByPk",
    "UpdateAttendanceUpdateEetschemaEventAttendeesByPk",
    "UpdateManyAttendanceInsertEetschemaEventAttendeesReturning",
    "WhereEventAttendee",
    "CreateEventAttendee",
    "OrderEventAttendee",
    "UpdateEventAttendee",
]
