from typing import Optional

from .base_model import BaseModel
from .fragments import SettlementFields


class GetSettlementSubscription(BaseModel):
    eetschema_settlements_by_pk: Optional[
        "GetSettlementSubscriptionEetschemaSettlementsByPk"
    ]


class GetSettlementSubscriptionEetschemaSettlementsByPk(SettlementFields):
    pass


GetSettlementSubscription.model_rebuild()
