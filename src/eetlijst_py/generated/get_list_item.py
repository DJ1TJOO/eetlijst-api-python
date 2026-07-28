from typing import Optional

from .base_model import BaseModel
from .fragments import ListItemFields


class GetListItem(BaseModel):
    eetschema_list_by_pk: Optional["GetListItemEetschemaListByPk"]


class GetListItemEetschemaListByPk(ListItemFields):
    pass


GetListItem.model_rebuild()
