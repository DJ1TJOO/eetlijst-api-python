from typing import Optional

from .base_model import BaseModel
from .fragments import GroupFields, UserInGroupFields


class GetGroupSubscription(BaseModel):
    eetschema_group_by_pk: Optional["GetGroupSubscriptionEetschemaGroupByPk"]


class GetGroupSubscriptionEetschemaGroupByPk(GroupFields):
    users_in_groups: Optional[
        list["GetGroupSubscriptionEetschemaGroupByPkUsersInGroups"]
    ] = None


class GetGroupSubscriptionEetschemaGroupByPkUsersInGroups(UserInGroupFields):
    pass


GetGroupSubscription.model_rebuild()
GetGroupSubscriptionEetschemaGroupByPk.model_rebuild()
