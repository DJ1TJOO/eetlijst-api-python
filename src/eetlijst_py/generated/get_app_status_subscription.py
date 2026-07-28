from .base_model import BaseModel
from .fragments import AppStatusFields


class GetAppStatusSubscription(BaseModel):
    eetschema_app_status: list["GetAppStatusSubscriptionEetschemaAppStatus"]


class GetAppStatusSubscriptionEetschemaAppStatus(AppStatusFields):
    pass


GetAppStatusSubscription.model_rebuild()
