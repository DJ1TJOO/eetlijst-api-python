from typing import Optional

from .base_model import BaseModel


class GetEventAttendeesViewSubscription(BaseModel):
    eetschema_event_attendees_view: list[
        "GetEventAttendeesViewSubscriptionEetschemaEventAttendeesView"
    ]


class GetEventAttendeesViewSubscriptionEetschemaEventAttendeesView(BaseModel):
    event_id: Optional[str]
    group_id: Optional[str]
    user_id: Optional[str]
    status: Optional[str]
    number_guests: Optional[int]
    comment: Optional[str]
    active: Optional[bool]
    order: Optional[int]
    monday: Optional[str]
    tuesday: Optional[str]
    wednesday: Optional[str]
    thursday: Optional[str]
    friday: Optional[str]
    saturday: Optional[str]
    sunday: Optional[str]


GetEventAttendeesViewSubscription.model_rebuild()
