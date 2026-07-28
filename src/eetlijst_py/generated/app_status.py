from .base_model import BaseModel
from .fragments import AppStatusFields


class AppStatus(BaseModel):
    eetschema_app_status: list["AppStatusEetschemaAppStatus"]


class AppStatusEetschemaAppStatus(AppStatusFields):
    pass


AppStatus.model_rebuild()
