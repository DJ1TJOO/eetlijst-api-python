from typing import Optional

from .base_model import BaseModel
from .fragments import UserFields


class UpdateUser(BaseModel):
    update_eetschema_user_by_pk: Optional["UpdateUserUpdateEetschemaUserByPk"]


class UpdateUserUpdateEetschemaUserByPk(UserFields):
    pass


UpdateUser.model_rebuild()
