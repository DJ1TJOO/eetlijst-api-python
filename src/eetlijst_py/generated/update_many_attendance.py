from typing import Optional

from .base_model import BaseModel
from .fragments import AttendanceFields


class UpdateManyAttendance(BaseModel):
    insert_eetschema_event_attendees: Optional[
        "UpdateManyAttendanceInsertEetschemaEventAttendees"
    ]


class UpdateManyAttendanceInsertEetschemaEventAttendees(BaseModel):
    returning: list["UpdateManyAttendanceInsertEetschemaEventAttendeesReturning"]


class UpdateManyAttendanceInsertEetschemaEventAttendeesReturning(AttendanceFields):
    pass


UpdateManyAttendance.model_rebuild()
UpdateManyAttendanceInsertEetschemaEventAttendees.model_rebuild()
