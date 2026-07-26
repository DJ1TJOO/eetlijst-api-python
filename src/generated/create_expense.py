from typing import Optional

from .base_model import BaseModel
from .fragments import ExpenseFields


class CreateExpense(BaseModel):
    insert_eetschema_expense_one: Optional["CreateExpenseInsertEetschemaExpenseOne"]


class CreateExpenseInsertEetschemaExpenseOne(ExpenseFields):
    pass


CreateExpense.model_rebuild()
