from typing import Optional

from .base_model import BaseModel


class GroupImportExpenseTotalSubscription(BaseModel):
    eetschema_expense_eetlijst_import_aggregate: (
        "GroupImportExpenseTotalSubscriptionEetschemaExpenseEetlijstImportAggregate"
    )


class GroupImportExpenseTotalSubscriptionEetschemaExpenseEetlijstImportAggregate(
    BaseModel
):
    aggregate: Optional[
        "GroupImportExpenseTotalSubscriptionEetschemaExpenseEetlijstImportAggregateAggregate"
    ]


class GroupImportExpenseTotalSubscriptionEetschemaExpenseEetlijstImportAggregateAggregate(
    BaseModel
):
    sum: Optional[
        "GroupImportExpenseTotalSubscriptionEetschemaExpenseEetlijstImportAggregateAggregateSum"
    ]


class GroupImportExpenseTotalSubscriptionEetschemaExpenseEetlijstImportAggregateAggregateSum(
    BaseModel
):
    payed_amount: Optional[int]


GroupImportExpenseTotalSubscription.model_rebuild()
GroupImportExpenseTotalSubscriptionEetschemaExpenseEetlijstImportAggregate.model_rebuild()
GroupImportExpenseTotalSubscriptionEetschemaExpenseEetlijstImportAggregateAggregate.model_rebuild()
