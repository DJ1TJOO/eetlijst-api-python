from typing import Optional

from .base_model import BaseModel
from .fragments import SettlementFields


class GetSettlement(BaseModel):
    eetschema_settlements_by_pk: Optional["GetSettlementEetschemaSettlementsByPk"]


class GetSettlementEetschemaSettlementsByPk(SettlementFields):
    pass


GetSettlement.model_rebuild()
