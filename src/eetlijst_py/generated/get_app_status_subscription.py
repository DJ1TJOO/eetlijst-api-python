from datetime import datetime

from .base_model import BaseModel


class GetAppStatusSubscription(BaseModel):
    eetschema_app_status: list["GetAppStatusSubscriptionEetschemaAppStatus"]


class GetAppStatusSubscriptionEetschemaAppStatus(BaseModel):
    id: str
    beta_online: bool
    created_at: datetime
    updated_at: datetime


GetAppStatusSubscription.model_rebuild()
