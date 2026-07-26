from typing import Optional

from .base_model import BaseModel


class GroupTotalExpense(BaseModel):
    eetschema_expense_aggregate: "GroupTotalExpenseEetschemaExpenseAggregate"
    eetschema_expense_eetlijst_import_aggregate: (
        "GroupTotalExpenseEetschemaExpenseEetlijstImportAggregate"
    )


class GroupTotalExpenseEetschemaExpenseAggregate(BaseModel):
    aggregate: Optional["GroupTotalExpenseEetschemaExpenseAggregateAggregate"]


class GroupTotalExpenseEetschemaExpenseAggregateAggregate(BaseModel):
    sum: Optional["GroupTotalExpenseEetschemaExpenseAggregateAggregateSum"]


class GroupTotalExpenseEetschemaExpenseAggregateAggregateSum(BaseModel):
    payed_amount: Optional[int]


class GroupTotalExpenseEetschemaExpenseEetlijstImportAggregate(BaseModel):
    aggregate: Optional[
        "GroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregate"
    ]


class GroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregate(BaseModel):
    sum: Optional[
        "GroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregateSum"
    ]


class GroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregateSum(BaseModel):
    payed_amount: Optional[int]


GroupTotalExpense.model_rebuild()
GroupTotalExpenseEetschemaExpenseAggregate.model_rebuild()
GroupTotalExpenseEetschemaExpenseAggregateAggregate.model_rebuild()
GroupTotalExpenseEetschemaExpenseEetlijstImportAggregate.model_rebuild()
GroupTotalExpenseEetschemaExpenseEetlijstImportAggregateAggregate.model_rebuild()
