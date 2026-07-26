from .base_model import BaseModel
from .fragments import ExpenseFields


class AllExpenses(BaseModel):
    eetschema_expense: list["AllExpensesEetschemaExpense"]


class AllExpensesEetschemaExpense(ExpenseFields):
    pass


AllExpenses.model_rebuild()
