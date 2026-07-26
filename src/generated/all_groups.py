from typing import Optional

from .base_model import BaseModel
from .fragments import GroupFields, UserInGroupFields


class AllGroups(BaseModel):
    eetschema_users_in_group: list["AllGroupsEetschemaUsersInGroup"]


class AllGroupsEetschemaUsersInGroup(BaseModel):
    group: "AllGroupsEetschemaUsersInGroupGroup"


class AllGroupsEetschemaUsersInGroupGroup(GroupFields):
    users_in_groups: Optional[
        list["AllGroupsEetschemaUsersInGroupGroupUsersInGroups"]
    ] = None


class AllGroupsEetschemaUsersInGroupGroupUsersInGroups(UserInGroupFields):
    pass


AllGroups.model_rebuild()
AllGroupsEetschemaUsersInGroup.model_rebuild()
AllGroupsEetschemaUsersInGroupGroup.model_rebuild()
