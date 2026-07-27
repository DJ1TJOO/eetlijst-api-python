from .base_model import BaseModel
from .fragments import ItemFields


class ListItems(BaseModel):
    eetschema_list: list["ListItemsEetschemaList"]


class ListItemsEetschemaList(ItemFields):
    pass


ListItems.model_rebuild()
