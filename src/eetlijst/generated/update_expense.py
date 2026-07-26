from typing import Optional

from .base_model import BaseModel
from .fragments import ExpenseFields


class UpdateExpense(BaseModel):
    update_eetschema_expense: Optional["UpdateExpenseUpdateEetschemaExpense"]


class UpdateExpenseUpdateEetschemaExpense(BaseModel):
    returning: list["UpdateExpenseUpdateEetschemaExpenseReturning"]


class UpdateExpenseUpdateEetschemaExpenseReturning(ExpenseFields):
    pass


UpdateExpense.model_rebuild()
UpdateExpenseUpdateEetschemaExpense.model_rebuild()
