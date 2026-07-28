"""Settlements service type exports."""

from datetime import datetime
from typing import Optional, TypedDict

from pydantic import BaseModel, ConfigDict

from eetlijst_py.generated.all_settlements import AllSettlementsEetschemaSettlements
from eetlijst_py.generated.create_settlement import (
    CreateSettlementSettlement,
)
from eetlijst_py.generated.fragments import (
    ExpenseFields,
    SettlementFields,
    SettlementFieldsAdjustmentsTotal,
    SettlementFieldsAdjustmentsTotalAggregate,
    SettlementFieldsAdjustmentsTotalAggregateSum,
    SettlementFieldsCreatedBy,
    SettlementFieldsExpensesTotal,
    SettlementFieldsExpensesTotalAggregate,
    SettlementFieldsExpensesTotalAggregateSum,
)
from eetlijst_py.generated.get_settlement import GetSettlementEetschemaSettlementsByPk
from eetlijst_py.generated.input_types import (
    eetschema_settlements_bool_exp as _eetschema_settlements_bool_exp,
)
from eetlijst_py.generated.input_types import (
    eetschema_settlements_order_by as _eetschema_settlements_order_by,
)
from eetlijst_py.generated.settle_unsettled_expenses import (
    SettleUnsettledExpensesUpdateEetschemaExpenseExpenses,
)
from eetlijst_py.generated.settlement_expenses import (
    SettlementExpensesEetschemaExpense,
)


class Settle(TypedDict):
    id: str
    expenses: list[ExpenseFields]
    adjustments: list[ExpenseFields]


class Settlement(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str
    group_id: str
    created_at: datetime
    updated_at: datetime
    created_by: SettlementFieldsCreatedBy
    expenses_total: Optional[int] = None
    adjustments_total: Optional[int] = None


WhereSettlement = _eetschema_settlements_bool_exp
OrderSettlement = _eetschema_settlements_order_by

__all__ = [
    "Settle",
    "Settlement",
    "SettlementFields",
    "SettlementFieldsAdjustmentsTotal",
    "SettlementFieldsAdjustmentsTotalAggregate",
    "SettlementFieldsAdjustmentsTotalAggregateSum",
    "SettlementFieldsCreatedBy",
    "SettlementFieldsExpensesTotal",
    "SettlementFieldsExpensesTotalAggregate",
    "SettlementFieldsExpensesTotalAggregateSum",
    "AllSettlementsEetschemaSettlements",
    "GetSettlementEetschemaSettlementsByPk",
    "CreateSettlementSettlement",
    "SettlementExpensesEetschemaExpense",
    "SettleUnsettledExpensesUpdateEetschemaExpenseExpenses",
    "WhereSettlement",
    "OrderSettlement",
]
