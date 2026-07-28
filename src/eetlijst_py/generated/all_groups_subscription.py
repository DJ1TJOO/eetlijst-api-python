from typing import Optional

from .base_model import BaseModel
from .fragments import GroupFields, UserInGroupFields


class AllGroupsSubscription(BaseModel):
    eetschema_group: list["AllGroupsSubscriptionEetschemaGroup"]


class AllGroupsSubscriptionEetschemaGroup(GroupFields):
    users_in_groups: Optional[
        list["AllGroupsSubscriptionEetschemaGroupUsersInGroups"]
    ] = None


class AllGroupsSubscriptionEetschemaGroupUsersInGroups(UserInGroupFields):
    pass


AllGroupsSubscription.model_rebuild()
AllGroupsSubscriptionEetschemaGroup.model_rebuild()
