from typing import Optional

from .base_model import BaseModel
from .fragments import GroupFields


class UpdateGroup(BaseModel):
    group: Optional["UpdateGroupGroup"]


class UpdateGroupGroup(GroupFields):
    pass


UpdateGroup.model_rebuild()
