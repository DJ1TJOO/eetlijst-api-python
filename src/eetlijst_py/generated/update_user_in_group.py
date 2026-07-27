from typing import Optional

from .base_model import BaseModel
from .fragments import UserInGroupFields


class UpdateUserInGroup(BaseModel):
    update_eetschema_users_in_group_by_pk: Optional[
        "UpdateUserInGroupUpdateEetschemaUsersInGroupByPk"
    ]


class UpdateUserInGroupUpdateEetschemaUsersInGroupByPk(UserInGroupFields):
    pass


UpdateUserInGroup.model_rebuild()
