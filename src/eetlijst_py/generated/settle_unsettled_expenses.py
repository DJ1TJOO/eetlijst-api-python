from typing import Optional

from .base_model import BaseModel
from .fragments import ExpenseFields


class SettleUnsettledExpenses(BaseModel):
    update_eetschema_expense: Optional["SettleUnsettledExpensesUpdateEetschemaExpense"]


class SettleUnsettledExpensesUpdateEetschemaExpense(BaseModel):
    number_expenses: int
    expenses: list["SettleUnsettledExpensesUpdateEetschemaExpenseExpenses"]


class SettleUnsettledExpensesUpdateEetschemaExpenseExpenses(ExpenseFields):
    pass


SettleUnsettledExpenses.model_rebuild()
SettleUnsettledExpensesUpdateEetschemaExpense.model_rebuild()
