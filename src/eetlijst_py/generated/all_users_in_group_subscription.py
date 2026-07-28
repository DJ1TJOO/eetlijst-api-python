from typing import Optional

from .base_model import BaseModel
from .fragments import UserInGroupFields


class AllUsersInGroupSubscription(BaseModel):
    eetschema_group_by_pk: Optional["AllUsersInGroupSubscriptionEetschemaGroupByPk"]


class AllUsersInGroupSubscriptionEetschemaGroupByPk(BaseModel):
    users_in_groups: list["AllUsersInGroupSubscriptionEetschemaGroupByPkUsersInGroups"]


class AllUsersInGroupSubscriptionEetschemaGroupByPkUsersInGroups(UserInGroupFields):
    pass


AllUsersInGroupSubscription.model_rebuild()
AllUsersInGroupSubscriptionEetschemaGroupByPk.model_rebuild()
