from .base_model import BaseModel
from .fragments import AppStatusFields


class AppStatusSubscription(BaseModel):
    eetschema_app_status: list["AppStatusSubscriptionEetschemaAppStatus"]


class AppStatusSubscriptionEetschemaAppStatus(AppStatusFields):
    pass


AppStatusSubscription.model_rebuild()
