from typing import Optional

from .base_model import BaseModel


class GroupExpenseTotalSubscription(BaseModel):
    eetschema_expense_aggregate: (
        "GroupExpenseTotalSubscriptionEetschemaExpenseAggregate"
    )


class GroupExpenseTotalSubscriptionEetschemaExpenseAggregate(BaseModel):
    aggregate: Optional[
        "GroupExpenseTotalSubscriptionEetschemaExpenseAggregateAggregate"
    ]


class GroupExpenseTotalSubscriptionEetschemaExpenseAggregateAggregate(BaseModel):
    sum: Optional["GroupExpenseTotalSubscriptionEetschemaExpenseAggregateAggregateSum"]


class GroupExpenseTotalSubscriptionEetschemaExpenseAggregateAggregateSum(BaseModel):
    payed_amount: Optional[int]


GroupExpenseTotalSubscription.model_rebuild()
GroupExpenseTotalSubscriptionEetschemaExpenseAggregate.model_rebuild()
GroupExpenseTotalSubscriptionEetschemaExpenseAggregateAggregate.model_rebuild()
