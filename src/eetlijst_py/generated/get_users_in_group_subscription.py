from datetime import datetime
from typing import Optional

from .base_model import BaseModel


class GetUsersInGroupSubscription(BaseModel):
    eetschema_users_in_group: list["GetUsersInGroupSubscriptionEetschemaUsersInGroup"]


class GetUsersInGroupSubscriptionEetschemaUsersInGroup(BaseModel):
    group_id: str
    user_id: str
    active: bool
    order: Optional[int]
    start_holliday: Optional[datetime]
    end_holliday: Optional[datetime]
    monday: Optional[str]
    tuesday: Optional[str]
    wednesday: Optional[str]
    thursday: Optional[str]
    friday: Optional[str]
    saturday: Optional[str]
    sunday: Optional[str]
    user: "GetUsersInGroupSubscriptionEetschemaUsersInGroupUser"


class GetUsersInGroupSubscriptionEetschemaUsersInGroupUser(BaseModel):
    id: str
    name: str
    email: Optional[str]
    allergies: list[str]
    birthday: Optional[datetime]
    profile_image: Optional[str]
    order_of_buttom_bar: Optional[list[str]]
    wants_to_recieve_notifications: bool
    funnel_lead: Optional[list[str]]


GetUsersInGroupSubscription.model_rebuild()
GetUsersInGroupSubscriptionEetschemaUsersInGroup.model_rebuild()
