from .base_model import BaseModel
from .fragments import UserFieldsPrivate


class GetUser(BaseModel):
    eetschema_user_private: list["GetUserEetschemaUserPrivate"]


class GetUserEetschemaUserPrivate(UserFieldsPrivate):
    pass


GetUser.model_rebuild()
