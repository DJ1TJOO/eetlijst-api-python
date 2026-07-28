from typing import Optional

from .base_model import BaseModel
from .fragments import ListItemFields


class CreateManyListItems(BaseModel):
    insert_eetschema_list: Optional["CreateManyListItemsInsertEetschemaList"]


class CreateManyListItemsInsertEetschemaList(BaseModel):
    returning: list["CreateManyListItemsInsertEetschemaListReturning"]


class CreateManyListItemsInsertEetschemaListReturning(ListItemFields):
    pass


CreateManyListItems.model_rebuild()
CreateManyListItemsInsertEetschemaList.model_rebuild()
