from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class JoinGroup(BaseModel):
    join_group: Optional["JoinGroupJoinGroup"] = Field(alias="joinGroup")


class JoinGroupJoinGroup(BaseModel):
    accepted: bool
    error: Optional[str]


JoinGroup.model_rebuild()
