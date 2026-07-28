from datetime import datetime
from typing import Optional

from .base_model import BaseModel


class GetExpensesSubscription(BaseModel):
    eetschema_expense: list["GetExpensesSubscriptionEetschemaExpense"]


class GetExpensesSubscriptionEetschemaExpense(BaseModel):
    id: str
    group_id: str
    description: str
    payed_amount: int
    payed_at: datetime
    payed_by: str
    issued_by: str
    event_id: Optional[str]
    settlement_expense_id: Optional[str]
    settled_id: Optional[str]
    deleted: bool
    created_at: datetime
    updated_at: datetime
    updated_by: Optional[str]
    expense_distributions: list[
        "GetExpensesSubscriptionEetschemaExpenseExpenseDistributions"
    ]


class GetExpensesSubscriptionEetschemaExpenseExpenseDistributions(BaseModel):
    id: str
    expense_id: str
    user_id: str
    payed_amount: int
    count: int
    created_at: datetime
    updated_at: datetime


GetExpensesSubscription.model_rebuild()
GetExpensesSubscriptionEetschemaExpense.model_rebuild()
