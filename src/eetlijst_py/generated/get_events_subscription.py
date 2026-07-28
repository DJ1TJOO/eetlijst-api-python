from datetime import datetime
from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetEventsSubscription(BaseModel):
    eetschema_event: list["GetEventsSubscriptionEetschemaEvent"]


class GetEventsSubscriptionEetschemaEvent(BaseModel):
    id: str
    group_id: str
    name: str
    description: Optional[str]
    type_: str = Field(alias="type")
    open: bool
    start_date: datetime
    end_date: datetime
    signup_deadline: Optional[datetime]
    changed_signup_time: bool
    created_by: Optional[str]
    closed_by: Optional[str]
    expense_id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


GetEventsSubscription.model_rebuild()
