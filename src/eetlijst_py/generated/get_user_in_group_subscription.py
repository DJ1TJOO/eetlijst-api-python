from typing import Optional

from .base_model import BaseModel
from .fragments import UserInGroupFields


class GetUserInGroupSubscription(BaseModel):
    eetschema_group_by_pk: Optional["GetUserInGroupSubscriptionEetschemaGroupByPk"]


class GetUserInGroupSubscriptionEetschemaGroupByPk(BaseModel):
    users_in_groups: list["GetUserInGroupSubscriptionEetschemaGroupByPkUsersInGroups"]


class GetUserInGroupSubscriptionEetschemaGroupByPkUsersInGroups(UserInGroupFields):
    pass


GetUserInGroupSubscription.model_rebuild()
GetUserInGroupSubscriptionEetschemaGroupByPk.model_rebuild()
