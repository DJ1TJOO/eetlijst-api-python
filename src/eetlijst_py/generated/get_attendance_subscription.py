from typing import Optional

from .base_model import BaseModel
from .fragments import AttendanceFields


class GetAttendanceSubscription(BaseModel):
    eetschema_event_attendees_by_pk: Optional[
        "GetAttendanceSubscriptionEetschemaEventAttendeesByPk"
    ]


class GetAttendanceSubscriptionEetschemaEventAttendeesByPk(AttendanceFields):
    pass


GetAttendanceSubscription.model_rebuild()
