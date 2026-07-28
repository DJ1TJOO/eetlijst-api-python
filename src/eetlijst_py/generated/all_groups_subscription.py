from typing import Optional

from .base_model import BaseModel
from .fragments import GroupFields, UserInGroupFields


class AllGroupsSubscription(BaseModel):
    eetschema_users_in_group: list["AllGroupsSubscriptionEetschemaUsersInGroup"]


class AllGroupsSubscriptionEetschemaUsersInGroup(BaseModel):
    group: "AllGroupsSubscriptionEetschemaUsersInGroupGroup"


class AllGroupsSubscriptionEetschemaUsersInGroupGroup(GroupFields):
    users_in_groups: Optional[
        list["AllGroupsSubscriptionEetschemaUsersInGroupGroupUsersInGroups"]
    ] = None


class AllGroupsSubscriptionEetschemaUsersInGroupGroupUsersInGroups(UserInGroupFields):
    pass


AllGroupsSubscription.model_rebuild()
AllGroupsSubscriptionEetschemaUsersInGroup.model_rebuild()
AllGroupsSubscriptionEetschemaUsersInGroupGroup.model_rebuild()
