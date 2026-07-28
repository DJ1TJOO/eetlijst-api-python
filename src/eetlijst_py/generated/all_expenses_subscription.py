from .base_model import BaseModel
from .fragments import ExpenseFields


class AllExpensesSubscription(BaseModel):
    eetschema_expense: list["AllExpensesSubscriptionEetschemaExpense"]


class AllExpensesSubscriptionEetschemaExpense(ExpenseFields):
    pass


AllExpensesSubscription.model_rebuild()
