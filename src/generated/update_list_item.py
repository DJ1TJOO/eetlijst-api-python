from typing import Optional

from .base_model import BaseModel
from .fragments import ItemFields


class UpdateListItem(BaseModel):
    update_eetschema_list_by_pk: Optional["UpdateListItemUpdateEetschemaListByPk"]


class UpdateListItemUpdateEetschemaListByPk(ItemFields):
    pass


UpdateListItem.model_rebuild()
