from typing import Optional

from .base_model import BaseModel
from .fragments import ExpenseFields


class GetExpense(BaseModel):
    eetschema_expense_by_pk: Optional["GetExpenseEetschemaExpenseByPk"]


class GetExpenseEetschemaExpenseByPk(ExpenseFields):
    pass


GetExpense.model_rebuild()
