from typing import Optional

from .base_model import BaseModel
from .fragments import ItemFields


class CreateManyListItems(BaseModel):
    insert_eetschema_list: Optional["CreateManyListItemsInsertEetschemaList"]


class CreateManyListItemsInsertEetschemaList(BaseModel):
    returning: list["CreateManyListItemsInsertEetschemaListReturning"]


class CreateManyListItemsInsertEetschemaListReturning(ItemFields):
    pass


CreateManyListItems.model_rebuild()
CreateManyListItemsInsertEetschemaList.model_rebuild()
