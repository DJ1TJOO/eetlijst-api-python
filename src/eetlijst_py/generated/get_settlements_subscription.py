from datetime import datetime

from .base_model import BaseModel


class GetSettlementsSubscription(BaseModel):
    eetschema_settlements: list["GetSettlementsSubscriptionEetschemaSettlements"]


class GetSettlementsSubscriptionEetschemaSettlements(BaseModel):
    id: str
    group_id: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    expenses: list["GetSettlementsSubscriptionEetschemaSettlementsExpenses"]
    group: "GetSettlementsSubscriptionEetschemaSettlementsGroup"
    user: "GetSettlementsSubscriptionEetschemaSettlementsUser"


class GetSettlementsSubscriptionEetschemaSettlementsExpenses(BaseModel):
    id: str
    description: str
    payed_amount: int


class GetSettlementsSubscriptionEetschemaSettlementsGroup(BaseModel):
    id: str
    name: str


class GetSettlementsSubscriptionEetschemaSettlementsUser(BaseModel):
    id: str
    name: str


GetSettlementsSubscription.model_rebuild()
GetSettlementsSubscriptionEetschemaSettlements.model_rebuild()
