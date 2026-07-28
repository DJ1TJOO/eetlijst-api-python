"""Expenses service type exports."""

from typing import TypedDict

from eetlijst_py.generated.all_expenses import AllExpensesEetschemaExpense
from eetlijst_py.generated.create_expense import CreateExpenseInsertEetschemaExpenseOne
from eetlijst_py.generated.fragments import (
    ExpenseFields,
    ExpenseFieldsExpenseDistributions,
    ExpenseFieldsExpenseDistributionsUser,
    ExpenseFieldsPayedBy,
    ExpenseFieldsUpdatedBy,
)
from eetlijst_py.generated.get_expense import GetExpenseEetschemaExpenseByPk
from eetlijst_py.generated.get_group_total_expense import (
    GetGroupTotalExpenseEetschemaExpenseAggregateAggregateSum,
)
from eetlijst_py.generated.input_types import (
    eetschema_expense_bool_exp as _eetschema_expense_bool_exp,
)
from eetlijst_py.generated.input_types import (
    eetschema_expense_distribution_insert_input as _eetschema_expense_distribution_insert_input,
)
from eetlijst_py.generated.input_types import (
    eetschema_expense_insert_input as _eetschema_expense_insert_input,
)
from eetlijst_py.generated.input_types import (
    eetschema_expense_order_by as _eetschema_expense_order_by,
)
from eetlijst_py.generated.input_types import (
    eetschema_expense_set_input as _eetschema_expense_set_input,
)
from eetlijst_py.generated.update_expense import (
    UpdateExpenseUpdateEetschemaExpenseReturning,
)


class GroupTotalExpense(TypedDict):
    total: int
    expenses: int
    imported: int


Expense = ExpenseFields

WhereExpense = _eetschema_expense_bool_exp
CreateExpenseDistribution = _eetschema_expense_distribution_insert_input
CreateExpense = _eetschema_expense_insert_input
OrderExpense = _eetschema_expense_order_by
UpdateExpense = _eetschema_expense_set_input

__all__ = [
    "GroupTotalExpense",
    "Expense",
    "ExpenseFields",
    "ExpenseFieldsExpenseDistributions",
    "ExpenseFieldsExpenseDistributionsUser",
    "ExpenseFieldsPayedBy",
    "ExpenseFieldsUpdatedBy",
    "AllExpensesEetschemaExpense",
    "GetExpenseEetschemaExpenseByPk",
    "CreateExpenseInsertEetschemaExpenseOne",
    "UpdateExpenseUpdateEetschemaExpenseReturning",
    "GetGroupTotalExpenseEetschemaExpenseAggregateAggregateSum",
    "WhereExpense",
    "CreateExpenseDistribution",
    "CreateExpense",
    "OrderExpense",
    "UpdateExpense",
]
