from datetime import datetime
from typing import Optional

from .base_model import BaseModel


class GetGroupListSubscription(BaseModel):
    eetschema_list: list["GetGroupListSubscriptionEetschemaList"]


class GetGroupListSubscriptionEetschemaList(BaseModel):
    id: str
    group_id: str
    checked: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


GetGroupListSubscription.model_rebuild()
