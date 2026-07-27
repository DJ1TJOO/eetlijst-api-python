from typing import Optional

from .base_model import BaseModel
from .fragments import GroupFields, UserInGroupFields


class GetGroup(BaseModel):
    eetschema_group_by_pk: Optional["GetGroupEetschemaGroupByPk"]


class GetGroupEetschemaGroupByPk(GroupFields):
    users_in_groups: Optional[list["GetGroupEetschemaGroupByPkUsersInGroups"]] = None


class GetGroupEetschemaGroupByPkUsersInGroups(UserInGroupFields):
    pass


GetGroup.model_rebuild()
GetGroupEetschemaGroupByPk.model_rebuild()
