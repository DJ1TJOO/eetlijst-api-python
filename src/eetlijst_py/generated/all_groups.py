from typing import Optional

from .base_model import BaseModel
from .fragments import GroupFields, UserInGroupFields


class AllGroups(BaseModel):
    eetschema_group: list["AllGroupsEetschemaGroup"]


class AllGroupsEetschemaGroup(GroupFields):
    users_in_groups: Optional[list["AllGroupsEetschemaGroupUsersInGroups"]] = None


class AllGroupsEetschemaGroupUsersInGroups(UserInGroupFields):
    pass


AllGroups.model_rebuild()
AllGroupsEetschemaGroup.model_rebuild()
