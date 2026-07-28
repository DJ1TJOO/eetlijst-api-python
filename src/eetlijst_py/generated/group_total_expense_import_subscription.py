from typing import Optional

from .base_model import BaseModel


class GroupTotalExpenseImportSubscription(BaseModel):
    eetschema_expense_eetlijst_import_aggregate: (
        "GroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregate"
    )


class GroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregate(
    BaseModel
):
    aggregate: Optional[
        "GroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregate"
    ]


class GroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregate(
    BaseModel
):
    sum: Optional[
        "GroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregateSum"
    ]


class GroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregateSum(
    BaseModel
):
    payed_amount: Optional[int]


GroupTotalExpenseImportSubscription.model_rebuild()
GroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregate.model_rebuild()
GroupTotalExpenseImportSubscriptionEetschemaExpenseEetlijstImportAggregateAggregate.model_rebuild()
