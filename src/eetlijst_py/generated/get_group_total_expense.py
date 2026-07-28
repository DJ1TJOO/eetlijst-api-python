from typing import Optional

from .base_model import BaseModel


class GetGroupTotalExpense(BaseModel):
    eetschema_expense_aggregate: "GetGroupTotalExpenseEetschemaExpenseAggregate"
    eetschema_expense_eetlijst_import_aggregate: (
        "GetGroupTotalExpenseEetschemaExpenseEetlijstImportAggregate"
    )


class GetGroupTotalExpenseEetschemaExpenseAggregate(BaseModel):
    aggregate: Optional["GetGroupTotalExpenseEetschemaExpenseAggregateAggregate"]


class GetGroupTotalExpenseEetschemaExpenseAggregateAggregate(BaseModel):
    sum: Optional["GetGroupTotalExpenseEetschemaExpenseAggregateAggregateSum"]


class GetGroupTotalExpenseEetschemaExpenseAggregateAggregateSum(BaseModel):
    payed_amount: Optional[int]


class GetGroupTotalExpenseEetschemaExpenseEetlijstImportAggregate(BaseModel):
    aggregate: Optional[
        "GetGroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregate"
    ]


class GetGroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregate(BaseModel):
    sum: Optional[
        "GetGroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregateSum"
    ]


class GetGroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregateSum(
    BaseModel
):
    payed_amount: Optional[int]


GetGroupTotalExpense.model_rebuild()
GetGroupTotalExpenseEetschemaExpenseAggregate.model_rebuild()
GetGroupTotalExpenseEetschemaExpenseAggregateAggregate.model_rebuild()
GetGroupTotalExpenseEetschemaExpenseEetlijstImportAggregate.model_rebuild()
GetGroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregate.model_rebuild()
