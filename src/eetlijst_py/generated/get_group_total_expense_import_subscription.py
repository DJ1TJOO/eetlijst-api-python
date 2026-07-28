from typing import Optional

from .base_model import BaseModel


class GetGroupTotalExpenseImportSubscription(BaseModel):
    eetschema_expense_eetlijst_import_aggregate: (
        "GetGroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregate"
    )


class GetGroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregate(
    BaseModel
):
    aggregate: Optional[
        "GetGroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregate"
    ]


class GetGroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregate(
    BaseModel
):
    sum: Optional[
        "GetGroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregateSum"
    ]


class GetGroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregateSum(
    BaseModel
):
    payed_amount: Optional[int]


GetGroupTotalExpenseImportSubscription.model_rebuild()
GetGroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregate.model_rebuild()
GetGroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregate.model_rebuild()
