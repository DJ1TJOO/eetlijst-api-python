from typing import Optional

from .base_model import BaseModel
from .fragments import ItemFields


class CreateListItem(BaseModel):
    insert_eetschema_list_one: Optional["CreateListItemInsertEetschemaListOne"]


class CreateListItemInsertEetschemaListOne(ItemFields):
    pass


CreateListItem.model_rebuild()
