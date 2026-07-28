from .base_model import BaseModel
from .fragments import SettlementFields


class AllSettlementsSubscription(BaseModel):
    eetschema_settlements: list["AllSettlementsSubscriptionEetschemaSettlements"]


class AllSettlementsSubscriptionEetschemaSettlements(SettlementFields):
    pass


AllSettlementsSubscription.model_rebuild()
