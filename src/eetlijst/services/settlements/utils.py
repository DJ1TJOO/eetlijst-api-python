from typing import TypedDict

from eetlijst.generated.fragments import ExpenseFieldsExpenseDistributionsUser

from eetlijst.services.expenses.utils import UserBalance


class AdjustmentExpenseDistribution(TypedDict):
    user: ExpenseFieldsExpenseDistributionsUser
    count: int
    payed_amount: int
    user_id: str


class CalculatedAdjustmentExpense(TypedDict):
    payed_by: ExpenseFieldsExpenseDistributionsUser
    payed_amount: int
    expense_distributions: list[AdjustmentExpenseDistribution]


def calculate_adjustment_expenses(
    balances: list[UserBalance],
) -> list[CalculatedAdjustmentExpense]:
    creditors: list[UserBalance] = sorted(
        [
            UserBalance(user=b["user"], balance=b["balance"])
            for b in balances
            if b["balance"] > 0
        ],
        key=lambda b: b["balance"],
    )

    debtors: list[UserBalance] = sorted(
        [
            UserBalance(user=b["user"], balance=b["balance"])
            for b in balances
            if b["balance"] < 0
        ],
        key=lambda b: abs(b["balance"]),
        reverse=True,
    )

    results: list[CalculatedAdjustmentExpense] = []

    for creditor in creditors:
        distributions: list[AdjustmentExpenseDistribution] = []

        for debtor in debtors:
            amount = min(creditor["balance"], abs(debtor["balance"]))
            if amount <= 0:
                continue

            distributions.append(
                {
                    "user": debtor["user"],
                    "payed_amount": amount,
                    "user_id": debtor["user"].id,
                    "count": 0,
                }
            )

            creditor["balance"] -= amount
            debtor["balance"] += amount

        total = -sum(entry["payed_amount"] for entry in distributions)

        distributions.append(
            {
                "user": creditor["user"],
                "payed_amount": total,
                "user_id": creditor["user"].id,
                "count": 0,
            }
        )

        results.append(
            {
                "payed_by": creditor["user"],
                "payed_amount": total,
                "expense_distributions": distributions,
            }
        )

    return results
