from typing import Optional

from eetlijst_py.generated.fragments import (
    AttendanceFields,
)
from eetlijst_py.generated.update_attendance import UpdateAttendance
from eetlijst_py.generated.update_many_attendance import UpdateManyAttendance

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.event_attendance.types import Attendance


def transform_attendance(attendance: Optional[AttendanceFields]) -> Attendance:
    if not attendance:
        raise EetlijstException("Attendance not found")

    data = attendance.model_dump()

    # 'linked_event' -> 'event'
    if "linked_event" in data:
        data["event"] = data.pop("linked_event")

    # 'user_in_group' -> 'user'
    if "user_in_group" in data:
        data["user"] = data.pop("user_in_group")

    return Attendance(**data)


def transform_update_attendance(update: UpdateAttendance):
    if not update.update_eetschema_event_attendees_by_pk:
        raise EetlijstException("Failed to update attendance")

    return transform_attendance(update.update_eetschema_event_attendees_by_pk)


def transform_update_many_attendance(updates: UpdateManyAttendance):
    if not updates.insert_eetschema_event_attendees:
        raise EetlijstException("Failed to update attendance")

    return [
        transform_attendance(update)
        for update in updates.insert_eetschema_event_attendees.returning
    ]
