from .base_model import BaseModel
from .fragments import ExpenseFields


class SettlementExpensesSubscription(BaseModel):
    eetschema_expense: list["SettlementExpensesSubscriptionEetschemaExpense"]


class SettlementExpensesSubscriptionEetschemaExpense(ExpenseFields):
    pass


SettlementExpensesSubscription.model_rebuild()
