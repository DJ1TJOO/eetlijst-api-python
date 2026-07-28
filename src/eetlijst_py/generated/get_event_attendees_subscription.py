from datetime import datetime
from typing import Optional

from .base_model import BaseModel


class GetEventAttendeesSubscription(BaseModel):
    eetschema_event_attendees: list[
        "GetEventAttendeesSubscriptionEetschemaEventAttendees"
    ]


class GetEventAttendeesSubscriptionEetschemaEventAttendees(BaseModel):
    event_id: str
    user_id: str
    status: str
    number_guests: int
    comment: Optional[str]
    user_changed_status: bool
    created_at: datetime
    updated_at: datetime


GetEventAttendeesSubscription.model_rebuild()
