from .base_model import BaseModel
from .fragments import AttendanceFields


class AllAttendancesSubscription(BaseModel):
    eetschema_event_attendees: list["AllAttendancesSubscriptionEetschemaEventAttendees"]


class AllAttendancesSubscriptionEetschemaEventAttendees(AttendanceFields):
    pass


AllAttendancesSubscription.model_rebuild()
