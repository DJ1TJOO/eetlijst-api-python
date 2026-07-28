from typing import Optional

from .base_model import BaseModel
from .fragments import ExpenseFields


class GetExpenseSubscription(BaseModel):
    eetschema_expense_by_pk: Optional["GetExpenseSubscriptionEetschemaExpenseByPk"]


class GetExpenseSubscriptionEetschemaExpenseByPk(ExpenseFields):
    pass


GetExpenseSubscription.model_rebuild()
