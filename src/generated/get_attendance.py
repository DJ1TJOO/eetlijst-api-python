from typing import Optional

from .base_model import BaseModel
from .fragments import AttendanceFields


class GetAttendance(BaseModel):
    eetschema_event_attendees_by_pk: Optional[
        "GetAttendanceEetschemaEventAttendeesByPk"
    ]


class GetAttendanceEetschemaEventAttendeesByPk(AttendanceFields):
    pass


GetAttendance.model_rebuild()
