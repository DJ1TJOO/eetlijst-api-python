from typing import Optional

from eetlijst_py.generated.create_expense import CreateExpense
from eetlijst_py.generated.fragments import ExpenseFields
from eetlijst_py.generated.get_group_total_expense import GetGroupTotalExpense
from eetlijst_py.generated.get_group_total_expense_import_subscription import (
    GetGroupTotalExpenseImportSubscription,
)
from eetlijst_py.generated.get_group_total_expense_subscription import (
    GetGroupTotalExpenseSubscription,
)
from eetlijst_py.generated.update_expense import UpdateExpense

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.expenses.types import Expense, GroupTotalExpense


def transform_expense(expense: Optional[ExpenseFields]) -> Expense:
    if not expense:
        raise EetlijstException("Expense not found")

    return expense


def transform_create_expense(expense: CreateExpense) -> Expense:
    if not expense or not expense.insert_eetschema_expense_one:
        raise EetlijstException("Failed to create expense")

    return transform_expense(expense.insert_eetschema_expense_one)


def transform_update_expense(expense: UpdateExpense) -> Expense:
    if (
        not expense
        or not expense.update_eetschema_expense
        or not expense.update_eetschema_expense.returning
    ):
        raise EetlijstException("Failed to update expense")

    return transform_expense(expense.update_eetschema_expense.returning[0])


def _get_payed_amount(aggregate) -> int:
    if (
        aggregate
        and aggregate.aggregate
        and aggregate.aggregate.sum
        and aggregate.aggregate.sum.payed_amount is not None
    ):
        return aggregate.aggregate.sum.payed_amount

    return 0


def transform_group_total_expense(
    result: Optional[GetGroupTotalExpense],
) -> GroupTotalExpense:
    if not result:
        return {"total": 0, "expenses": 0, "imported": 0}

    expenses_total = _get_payed_amount(result.eetschema_expense_aggregate)
    imported_total = _get_payed_amount(
        result.eetschema_expense_eetlijst_import_aggregate
    )

    return {
        "total": expenses_total + imported_total,
        "expenses": expenses_total,
        "imported": imported_total,
    }


def transform_group_total_expense_subscription(
    expenses: Optional[GetGroupTotalExpenseSubscription],
    imported: Optional[GetGroupTotalExpenseImportSubscription],
) -> GroupTotalExpense:
    expenses_total = _get_payed_amount(
        expenses.eetschema_expense_aggregate if expenses else None
    )
    imported_total = _get_payed_amount(
        imported.eetschema_expense_eetlijst_import_aggregate if imported else None
    )

    return {
        "total": expenses_total + imported_total,
        "expenses": expenses_total,
        "imported": imported_total,
    }
