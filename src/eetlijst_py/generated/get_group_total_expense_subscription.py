from typing import Optional

from .base_model import BaseModel


class GetGroupTotalExpenseSubscription(BaseModel):
    eetschema_expense_aggregate: (
        "GetGroupTotalExpenseSubscriptionEetschemaExpenseAggregate"
    )


class GetGroupTotalExpenseSubscriptionEetschemaExpenseAggregate(BaseModel):
    aggregate: Optional[
        "GetGroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregate"
    ]


class GetGroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregate(BaseModel):
    sum: Optional[
        "GetGroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregateSum"
    ]


class GetGroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregateSum(BaseModel):
    payed_amount: Optional[int]


GetGroupTotalExpenseSubscription.model_rebuild()
GetGroupTotalExpenseSubscriptionEetschemaExpenseAggregate.model_rebuild()
GetGroupTotalExpenseSubscriptionEetschemaExpenseAggregateAggregate.model_rebuild()
