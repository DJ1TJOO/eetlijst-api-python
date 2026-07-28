from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from eetlijst_py.generated.create_settlement import CreateSettlement
from eetlijst_py.generated.fragments import (
    ExpenseFields,
    SettlementFields,
    SettlementFieldsCreatedBy,
)
from eetlijst_py.generated.settle_unsettled_expenses import SettleUnsettledExpenses
from eetlijst_py.generated.settlement_expenses import SettlementExpenses
from eetlijst_py.generated.settlement_expenses_subscription import (
    SettlementExpensesSubscription,
)

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.expenses.transformers import transform_expense


class SettlementResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str
    group_id: str
    created_at: datetime
    updated_at: datetime
    created_by: SettlementFieldsCreatedBy
    expenses_total: Optional[int] = None
    adjustments_total: Optional[int] = None


class SettleUnsettledExpensesResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    number_expenses: int
    expenses: list[ExpenseFields]


def transform_settlement(settlement: Optional[SettlementFields]) -> SettlementResult:
    if not settlement:
        raise EetlijstException("Settlement not found")

    expenses_total: Optional[int] = None
    if (
        settlement.expenses_total
        and settlement.expenses_total.aggregate
        and settlement.expenses_total.aggregate.sum
    ):
        expenses_total = settlement.expenses_total.aggregate.sum.payed_amount

    adjustments_total: Optional[int] = None
    if (
        settlement.adjustments_total
        and settlement.adjustments_total.aggregate
        and settlement.adjustments_total.aggregate.sum
    ):
        adjustments_total = settlement.adjustments_total.aggregate.sum.payed_amount

    data = {
        **settlement.model_dump(),
        "expenses_total": expenses_total,
        "adjustments_total": adjustments_total,
    }

    return SettlementResult(**data)


def transform_create_settlement(result: CreateSettlement) -> SettlementResult:
    if not result.settlement:
        raise EetlijstException("Failed to create settlement")

    return transform_settlement(result.settlement)


def transform_settle_unsettled_expenses(
    result: SettleUnsettledExpenses,
) -> SettleUnsettledExpensesResult:
    if not result.update_eetschema_expense:
        raise EetlijstException("Failed to settle expenses")

    expenses = [
        transform_expense(expense)
        for expense in result.update_eetschema_expense.expenses
    ]

    data = {
        **result.update_eetschema_expense.model_dump(),
        "expenses": expenses,
    }

    return SettleUnsettledExpensesResult(**data)


def transform_settlement_expenses(
    result: SettlementExpenses | SettlementExpensesSubscription,
):
    return [transform_expense(expense) for expense in result.eetschema_expense]
