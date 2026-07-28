from typing import Optional

from .base_model import BaseModel
from .fragments import ListItemFields


class CreateListItem(BaseModel):
    insert_eetschema_list_one: Optional["CreateListItemInsertEetschemaListOne"]


class CreateListItemInsertEetschemaListOne(ListItemFields):
    pass


CreateListItem.model_rebuild()
