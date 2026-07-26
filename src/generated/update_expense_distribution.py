from typing import Optional

from .base_model import BaseModel


class UpdateExpenseDistribution(BaseModel):
    delete_eetschema_expense_distribution: Optional[
        "UpdateExpenseDistributionDeleteEetschemaExpenseDistribution"
    ]
    insert_eetschema_expense_distribution: Optional[
        "UpdateExpenseDistributionInsertEetschemaExpenseDistribution"
    ]


class UpdateExpenseDistributionDeleteEetschemaExpenseDistribution(BaseModel):
    affected_rows: int


class UpdateExpenseDistributionInsertEetschemaExpenseDistribution(BaseModel):
    affected_rows: int


UpdateExpenseDistribution.model_rebuild()
