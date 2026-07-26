from typing import Optional

from .base_model import BaseModel
from .fragments import UserInGroupFields


class UpdateUsersInGroup(BaseModel):
    update_eetschema_users_in_group_many: Optional[
        list[Optional["UpdateUsersInGroupUpdateEetschemaUsersInGroupMany"]]
    ]


class UpdateUsersInGroupUpdateEetschemaUsersInGroupMany(BaseModel):
    number_users_in_group: int
    users_in_group: list[
        "UpdateUsersInGroupUpdateEetschemaUsersInGroupManyUsersInGroup"
    ]


class UpdateUsersInGroupUpdateEetschemaUsersInGroupManyUsersInGroup(UserInGroupFields):
    pass


UpdateUsersInGroup.model_rebuild()
UpdateUsersInGroupUpdateEetschemaUsersInGroupMany.model_rebuild()
