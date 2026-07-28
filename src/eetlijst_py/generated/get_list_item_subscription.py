from typing import Optional

from .base_model import BaseModel
from .fragments import ListItemFields


class GetListItemSubscription(BaseModel):
    eetschema_list_by_pk: Optional["GetListItemSubscriptionEetschemaListByPk"]


class GetListItemSubscriptionEetschemaListByPk(ListItemFields):
    pass


GetListItemSubscription.model_rebuild()
