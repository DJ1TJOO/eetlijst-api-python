from .base_model import BaseModel
from .fragments import ListItemFields


class ListItemsSubscription(BaseModel):
    eetschema_list: list["ListItemsSubscriptionEetschemaList"]


class ListItemsSubscriptionEetschemaList(ListItemFields):
    pass


ListItemsSubscription.model_rebuild()
