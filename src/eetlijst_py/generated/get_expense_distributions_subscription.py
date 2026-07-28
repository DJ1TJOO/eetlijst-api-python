from datetime import datetime

from .base_model import BaseModel


class GetExpenseDistributionsSubscription(BaseModel):
    eetschema_expense_distribution: list[
        "GetExpenseDistributionsSubscriptionEetschemaExpenseDistribution"
    ]


class GetExpenseDistributionsSubscriptionEetschemaExpenseDistribution(BaseModel):
    id: str
    expense_id: str
    user_id: str
    payed_amount: int
    count: int
    created_at: datetime
    updated_at: datetime


GetExpenseDistributionsSubscription.model_rebuild()
