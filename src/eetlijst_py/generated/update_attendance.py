from typing import Optional

from .base_model import BaseModel
from .fragments import AttendanceFields


class UpdateAttendance(BaseModel):
    update_eetschema_event_attendees_by_pk: Optional[
        "UpdateAttendanceUpdateEetschemaEventAttendeesByPk"
    ]


class UpdateAttendanceUpdateEetschemaEventAttendeesByPk(AttendanceFields):
    pass


UpdateAttendance.model_rebuild()
