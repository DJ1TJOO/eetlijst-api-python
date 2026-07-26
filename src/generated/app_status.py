from datetime import datetime

from .base_model import BaseModel


class AppStatus(BaseModel):
    eetschema_app_status: list["AppStatusEetschemaAppStatus"]


class AppStatusEetschemaAppStatus(BaseModel):
    id: str
    beta_online: bool
    updated_at: datetime


AppStatus.model_rebuild()
