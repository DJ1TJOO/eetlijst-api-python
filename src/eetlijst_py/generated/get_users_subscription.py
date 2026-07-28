from datetime import datetime
from typing import Optional

from .base_model import BaseModel


class GetUsersSubscription(BaseModel):
    eetschema_user: list["GetUsersSubscriptionEetschemaUser"]


class GetUsersSubscriptionEetschemaUser(BaseModel):
    id: str
    name: str
    origin: Optional[str]
    email: Optional[str]
    allergies: list[str]
    birthday: Optional[datetime]
    profile_image: Optional[str]
    order_of_buttom_bar: Optional[list[str]]
    wants_to_recieve_notifications: bool
    funnel_lead: Optional[list[str]]


GetUsersSubscription.model_rebuild()
