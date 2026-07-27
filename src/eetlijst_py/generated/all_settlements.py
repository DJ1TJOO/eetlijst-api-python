from .base_model import BaseModel
from .fragments import SettlementFields


class AllSettlements(BaseModel):
    eetschema_settlements: list["AllSettlementsEetschemaSettlements"]


class AllSettlementsEetschemaSettlements(SettlementFields):
    pass


AllSettlements.model_rebuild()
