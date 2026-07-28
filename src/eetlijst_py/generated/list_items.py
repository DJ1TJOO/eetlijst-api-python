from .base_model import BaseModel
from .fragments import ListItemFields


class ListItems(BaseModel):
    eetschema_list: list["ListItemsEetschemaList"]


class ListItemsEetschemaList(ListItemFields):
    pass


ListItems.model_rebuild()
