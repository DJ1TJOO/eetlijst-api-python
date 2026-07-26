from .base_model import BaseModel
from .fragments import ExpenseFields


class SettlementExpenses(BaseModel):
    eetschema_expense: list["SettlementExpensesEetschemaExpense"]


class SettlementExpensesEetschemaExpense(ExpenseFields):
    pass


SettlementExpenses.model_rebuild()
