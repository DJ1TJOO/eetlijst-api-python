from typing import Optional, TypedDict

from eetlijst_py.generated.create_expense import CreateExpense
from eetlijst_py.generated.fragments import ExpenseFields
from eetlijst_py.generated.group_total_expense import GroupTotalExpense
from eetlijst_py.generated.group_total_expense_import_subscription import (
    GroupTotalExpenseImportSubscription,
)
from eetlijst_py.generated.group_total_expense_subscription import (
    GroupTotalExpenseSubscription,
)
from eetlijst_py.generated.update_expense import UpdateExpense

from eetlijst_py.exceptions import EetlijstException


class GroupTotalExpenseDict(TypedDict):
    total: int
    expenses: int
    imported: int


def transform_expense(expense: Optional[ExpenseFields]) -> ExpenseFields:
    if not expense:
        raise EetlijstException("Expense not found")

    return expense


def transform_create_expense(expense: CreateExpense) -> ExpenseFields:
    if not expense or not expense.insert_eetschema_expense_one:
        raise EetlijstException("Failed to create expense")

    return transform_expense(expense.insert_eetschema_expense_one)


def transform_update_expense(expense: UpdateExpense) -> ExpenseFields:
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
    result: Optional[GroupTotalExpense],
) -> GroupTotalExpenseDict:
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
    expenses: Optional[GroupTotalExpenseSubscription],
    imported: Optional[GroupTotalExpenseImportSubscription],
) -> GroupTotalExpenseDict:
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
