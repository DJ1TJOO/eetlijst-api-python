from typing import Optional

from .base_model import BaseModel


class GroupTotalExpenseSubscription(BaseModel):
    eetschema_expense_aggregate: (
        "GroupTotalExpenseSubscriptionEetschemaExpenseAggregate"
    )


class GroupTotalExpenseSubscriptionEetschemaExpenseAggregate(BaseModel):
    aggregate: Optional[
        "GroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregate"
    ]


class GroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregate(BaseModel):
    sum: Optional["GroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregateSum"]


class GroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregateSum(BaseModel):
    payed_amount: Optional[int]


GroupTotalExpenseSubscription.model_rebuild()
GroupTotalExpenseSubscriptionEetschemaExpenseAggregate.model_rebuild()
GroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregate.model_rebuild()
