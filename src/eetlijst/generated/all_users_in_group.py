from typing import Optional

from .base_model import BaseModel
from .fragments import UserInGroupFields


class AllUsersInGroup(BaseModel):
    eetschema_group_by_pk: Optional["AllUsersInGroupEetschemaGroupByPk"]


class AllUsersInGroupEetschemaGroupByPk(BaseModel):
    users_in_groups: list["AllUsersInGroupEetschemaGroupByPkUsersInGroups"]


class AllUsersInGroupEetschemaGroupByPkUsersInGroups(UserInGroupFields):
    pass


AllUsersInGroup.model_rebuild()
AllUsersInGroupEetschemaGroupByPk.model_rebuild()
