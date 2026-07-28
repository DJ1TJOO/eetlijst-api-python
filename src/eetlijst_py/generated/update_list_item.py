from typing import Optional

from .base_model import BaseModel
from .fragments import ListItemFields


class UpdateListItem(BaseModel):
    update_eetschema_list_by_pk: Optional["UpdateListItemUpdateEetschemaListByPk"]


class UpdateListItemUpdateEetschemaListByPk(ListItemFields):
    pass


UpdateListItem.model_rebuild()
