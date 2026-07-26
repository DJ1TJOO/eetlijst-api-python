from typing import Optional

from .base_model import BaseModel
from .fragments import GroupFields


class CreateGroup(BaseModel):
    group: Optional["CreateGroupGroup"]


class CreateGroupGroup(GroupFields):
    pass


CreateGroup.model_rebuild()
