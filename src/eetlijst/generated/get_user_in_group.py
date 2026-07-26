from typing import Optional

from .base_model import BaseModel
from .fragments import UserInGroupFields


class GetUserInGroup(BaseModel):
    eetschema_group_by_pk: Optional["GetUserInGroupEetschemaGroupByPk"]


class GetUserInGroupEetschemaGroupByPk(BaseModel):
    users_in_groups: list["GetUserInGroupEetschemaGroupByPkUsersInGroups"]


class GetUserInGroupEetschemaGroupByPkUsersInGroups(UserInGroupFields):
    pass


GetUserInGroup.model_rebuild()
GetUserInGroupEetschemaGroupByPk.model_rebuild()
