from .base_model import BaseModel
from .fragments import AttendanceFields


class AllAttendances(BaseModel):
    eetschema_event_attendees: list["AllAttendancesEetschemaEventAttendees"]


class AllAttendancesEetschemaEventAttendees(AttendanceFields):
    pass


AllAttendances.model_rebuild()
