from .base_model import BaseModel
from .fragments import AppStatusFields


class GetAppStatus(BaseModel):
    eetschema_app_status: list["GetAppStatusEetschemaAppStatus"]


class GetAppStatusEetschemaAppStatus(AppStatusFields):
    pass


GetAppStatus.model_rebuild()
