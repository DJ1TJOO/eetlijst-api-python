from typing import TypedDict

from src.generated.fragments import ExpenseFields, ExpenseFieldsExpenseDistributionsUser


class UserBalance(TypedDict):
    user: ExpenseFieldsExpenseDistributionsUser
    balance: int


def calculate_balances_from_expenses(
    expenses: list[ExpenseFields],
) -> list[UserBalance]:
    balances: dict[str, UserBalance] = {}

    for expense in expenses:
        for distribution in expense.expense_distributions:
            user_id = distribution.user.id
            payed_amount = distribution.payed_amount

            if user_id in balances:
                balances[user_id]["balance"] += payed_amount
            else:
                balances[user_id] = {"user": distribution.user, "balance": payed_amount}

    result = list(balances.values())
    result.sort(key=lambda item: item["balance"], reverse=True)
    return result
