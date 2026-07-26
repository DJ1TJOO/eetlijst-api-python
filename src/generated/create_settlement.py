from typing import Optional

from .base_model import BaseModel
from .fragments import SettlementFields


class CreateSettlement(BaseModel):
    settlement: Optional["CreateSettlementSettlement"]


class CreateSettlementSettlement(SettlementFields):
    pass


CreateSettlement.model_rebuild()
