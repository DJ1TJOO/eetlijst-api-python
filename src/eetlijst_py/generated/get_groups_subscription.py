from datetime import datetime
from typing import Optional

from .base_model import BaseModel


class GetGroupsSubscription(BaseModel):
    eetschema_group: list["GetGroupsSubscriptionEetschemaGroup"]


class GetGroupsSubscriptionEetschemaGroup(BaseModel):
    id: str
    name: str
    description: Optional[str]
    address: Optional[str]
    city: Optional[str]
    email: Optional[str]
    login_name: Optional[str]
    active: bool
    beta: bool
    invite_open: bool
    invite_uuid: str
    default_status: Optional[str]
    default_close_time: Optional[datetime]
    pincode: Optional[int]
    statistics_start_date: Optional[datetime]
    statistics_end_date: Optional[datetime]
    created_at: datetime
    created_at_eetlijst: Optional[datetime]
    updated_at: datetime


GetGroupsSubscription.model_rebuild()
