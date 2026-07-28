from collections.abc import AsyncIterator
from datetime import datetime
from typing import Any, Optional, Union

from .all_attendances import AllAttendances
from .all_attendances_subscription import AllAttendancesSubscription
from .all_events import AllEvents
from .all_events_subscription import AllEventsSubscription
from .all_expenses import AllExpenses
from .all_expenses_subscription import AllExpensesSubscription
from .all_groups import AllGroups
from .all_groups_subscription import AllGroupsSubscription
from .all_settlements import AllSettlements
from .all_settlements_subscription import AllSettlementsSubscription
from .all_users_in_group import AllUsersInGroup
from .all_users_in_group_subscription import AllUsersInGroupSubscription
from .app_status import AppStatus
from .app_status_subscription import AppStatusSubscription
from .async_base_client import AsyncBaseClient
from .automatic_events import AutomaticEvents
from .base_model import UNSET, UnsetType
from .create_expense import CreateExpense
from .create_group import CreateGroup
from .create_list_item import CreateListItem
from .create_many_list_items import CreateManyListItems
from .create_settlement import CreateSettlement
from .get_attendance import GetAttendance
from .get_attendance_subscription import GetAttendanceSubscription
from .get_event import GetEvent
from .get_event_subscription import GetEventSubscription
from .get_expense import GetExpense
from .get_expense_subscription import GetExpenseSubscription
from .get_group import GetGroup
from .get_group_subscription import GetGroupSubscription
from .get_list_item import GetListItem
from .get_list_item_subscription import GetListItemSubscription
from .get_settlement import GetSettlement
from .get_settlement_subscription import GetSettlementSubscription
from .get_user import GetUser
from .get_user_in_group import GetUserInGroup
from .get_user_in_group_subscription import GetUserInGroupSubscription
from .get_user_subscription import GetUserSubscription
from .group_total_expense import GroupTotalExpense
from .group_total_expense_import_subscription import GroupTotalExpenseImportSubscription
from .group_total_expense_subscription import GroupTotalExpenseSubscription
from .input_types import (
    eetschema_event_attendees_bool_exp,
    eetschema_event_attendees_insert_input,
    eetschema_event_attendees_order_by,
    eetschema_event_attendees_set_input,
    eetschema_event_bool_exp,
    eetschema_event_order_by,
    eetschema_event_set_input,
    eetschema_expense_bool_exp,
    eetschema_expense_distribution_insert_input,
    eetschema_expense_order_by,
    eetschema_expense_set_input,
    eetschema_group_set_input,
    eetschema_list_bool_exp,
    eetschema_list_insert_input,
    eetschema_list_order_by,
    eetschema_list_set_input,
    eetschema_settlements_bool_exp,
    eetschema_settlements_order_by,
    eetschema_user_set_input,
    eetschema_users_in_group_bool_exp,
    eetschema_users_in_group_order_by,
    eetschema_users_in_group_set_input,
    eetschema_users_in_group_updates,
)
from .join_group import JoinGroup
from .list_items import ListItems
from .list_items_subscription import ListItemsSubscription
from .remove_account import RemoveAccount
from .settle_unsettled_expenses import SettleUnsettledExpenses
from .settlement_expenses import SettlementExpenses
from .settlement_expenses_subscription import SettlementExpensesSubscription
from .update_attendance import UpdateAttendance
from .update_event import UpdateEvent
from .update_expense import UpdateExpense
from .update_expense_distribution import UpdateExpenseDistribution
from .update_group import UpdateGroup
from .update_list_item import UpdateListItem
from .update_many_attendance import UpdateManyAttendance
from .update_user import UpdateUser
from .update_user_in_group import UpdateUserInGroup
from .update_users_in_group import UpdateUsersInGroup


def gql(q: str) -> str:
    return q


class GraphQlClient(AsyncBaseClient):
    async def app_status(self, **kwargs: Any) -> AppStatus:
        query = gql("""
            query AppStatus {
              eetschema_app_status {
                ...AppStatusFields
              }
            }

            fragment AppStatusFields on eetschema_app_status {
              id
              beta_online
              updated_at
            }
            """)
        variables: dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="AppStatus", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AppStatus.model_validate(data)

    async def app_status_subscription(
        self, **kwargs: Any
    ) -> AsyncIterator[AppStatusSubscription]:
        query = gql("""
            subscription AppStatusSubscription {
              eetschema_app_status {
                ...AppStatusFields
              }
            }

            fragment AppStatusFields on eetschema_app_status {
              id
              beta_online
              updated_at
            }
            """)
        variables: dict[str, object] = {}
        async for data in self.execute_ws(
            query=query,
            operation_name="AppStatusSubscription",
            variables=variables,
            **kwargs,
        ):
            yield AppStatusSubscription.model_validate(data)

    async def update_many_attendance(
        self, updates: list[eetschema_event_attendees_insert_input], **kwargs: Any
    ) -> UpdateManyAttendance:
        query = gql("""
            mutation UpdateManyAttendance($updates: [eetschema_event_attendees_insert_input!]!) {
              insert_eetschema_event_attendees(
                objects: $updates
                on_conflict: {constraint: event_attending_members_pkey, update_columns: [status, number_guests, user_changed_status, comment]}
              ) {
                returning {
                  ...AttendanceFields
                }
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }
            """)
        variables: dict[str, object] = {"updates": updates}
        response = await self.execute(
            query=query,
            operation_name="UpdateManyAttendance",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return UpdateManyAttendance.model_validate(data)

    async def update_attendance(
        self,
        event_id: str,
        user_id: str,
        set_: eetschema_event_attendees_set_input,
        **kwargs: Any,
    ) -> UpdateAttendance:
        query = gql("""
            mutation UpdateAttendance($eventId: uuid!, $userId: String!, $_set: eetschema_event_attendees_set_input!) {
              update_eetschema_event_attendees_by_pk(
                pk_columns: {event_id: $eventId, user_id: $userId}
                _set: $_set
              ) {
                ...AttendanceFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "eventId": event_id,
            "userId": user_id,
            "_set": set_,
        }
        response = await self.execute(
            query=query,
            operation_name="UpdateAttendance",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return UpdateAttendance.model_validate(data)

    async def all_attendances(
        self,
        where: Union[Optional[eetschema_event_attendees_bool_exp], UnsetType] = UNSET,
        order: Union[
            Optional[list[eetschema_event_attendees_order_by]], UnsetType
        ] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AllAttendances:
        query = gql("""
            query AllAttendances($where: eetschema_event_attendees_bool_exp, $order: [eetschema_event_attendees_order_by!], $limit: Int) {
              eetschema_event_attendees(where: $where, order_by: $order, limit: $limit) {
                ...AttendanceFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        response = await self.execute(
            query=query, operation_name="AllAttendances", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AllAttendances.model_validate(data)

    async def get_attendance(
        self, event_id: str, user_id: str, **kwargs: Any
    ) -> GetAttendance:
        query = gql("""
            query GetAttendance($eventId: uuid!, $userId: String!) {
              eetschema_event_attendees_by_pk(user_id: $userId, event_id: $eventId) {
                ...AttendanceFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }
            """)
        variables: dict[str, object] = {"eventId": event_id, "userId": user_id}
        response = await self.execute(
            query=query, operation_name="GetAttendance", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetAttendance.model_validate(data)

    async def all_attendances_subscription(
        self,
        where: Union[Optional[eetschema_event_attendees_bool_exp], UnsetType] = UNSET,
        order: Union[
            Optional[list[eetschema_event_attendees_order_by]], UnsetType
        ] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[AllAttendancesSubscription]:
        query = gql("""
            subscription AllAttendancesSubscription($where: eetschema_event_attendees_bool_exp, $order: [eetschema_event_attendees_order_by!], $limit: Int) {
              eetschema_event_attendees(where: $where, order_by: $order, limit: $limit) {
                ...AttendanceFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        async for data in self.execute_ws(
            query=query,
            operation_name="AllAttendancesSubscription",
            variables=variables,
            **kwargs,
        ):
            yield AllAttendancesSubscription.model_validate(data)

    async def get_attendance_subscription(
        self, event_id: str, user_id: str, **kwargs: Any
    ) -> AsyncIterator[GetAttendanceSubscription]:
        query = gql("""
            subscription GetAttendanceSubscription($eventId: uuid!, $userId: String!) {
              eetschema_event_attendees_by_pk(user_id: $userId, event_id: $eventId) {
                ...AttendanceFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }
            """)
        variables: dict[str, object] = {"eventId": event_id, "userId": user_id}
        async for data in self.execute_ws(
            query=query,
            operation_name="GetAttendanceSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GetAttendanceSubscription.model_validate(data)

    async def update_event(
        self,
        event_id: str,
        set_: eetschema_event_set_input,
        include_attendees: Union[Optional[bool], UnsetType] = UNSET,
        include_expenses: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> UpdateEvent:
        query = gql("""
            mutation UpdateEvent($eventId: uuid!, $_set: eetschema_event_set_input!, $includeAttendees: Boolean = false, $includeExpenses: Boolean = false) {
              update_eetschema_event_by_pk(pk_columns: {id: $eventId}, _set: $_set) {
                ...EventFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }

            fragment EventFields on eetschema_event {
              id
              group_id
              open
              start_date
              closed_by
              signup_deadline
              changed_signup_time
              name
              description
              user {
                id
                name
              }
              created_at
              updated_at
              linked_expenses @include(if: $includeExpenses) {
                ...ExpenseFields
              }
              event_attendees @include(if: $includeAttendees) {
                ...AttendanceFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {
            "eventId": event_id,
            "_set": set_,
            "includeAttendees": include_attendees,
            "includeExpenses": include_expenses,
        }
        response = await self.execute(
            query=query, operation_name="UpdateEvent", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateEvent.model_validate(data)

    async def all_events(
        self,
        where: Union[Optional[eetschema_event_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_event_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        include_attendees: Union[Optional[bool], UnsetType] = UNSET,
        include_expenses: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AllEvents:
        query = gql("""
            query AllEvents($where: eetschema_event_bool_exp, $order: [eetschema_event_order_by!], $limit: Int, $includeAttendees: Boolean = false, $includeExpenses: Boolean = false) {
              eetschema_event(where: $where, order_by: $order, limit: $limit) {
                ...EventFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }

            fragment EventFields on eetschema_event {
              id
              group_id
              open
              start_date
              closed_by
              signup_deadline
              changed_signup_time
              name
              description
              user {
                id
                name
              }
              created_at
              updated_at
              linked_expenses @include(if: $includeExpenses) {
                ...ExpenseFields
              }
              event_attendees @include(if: $includeAttendees) {
                ...AttendanceFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {
            "where": where,
            "order": order,
            "limit": limit,
            "includeAttendees": include_attendees,
            "includeExpenses": include_expenses,
        }
        response = await self.execute(
            query=query, operation_name="AllEvents", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AllEvents.model_validate(data)

    async def automatic_events(
        self, group_id: str, date: str, **kwargs: Any
    ) -> AutomaticEvents:
        query = gql("""
            query AutomaticEvents($groupId: uuid!, $date: String!) {
              queryTodaysEvents(group_id: $groupId, date: $date) {
                id
              }
            }
            """)
        variables: dict[str, object] = {"groupId": group_id, "date": date}
        response = await self.execute(
            query=query, operation_name="AutomaticEvents", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AutomaticEvents.model_validate(data)

    async def get_event(
        self,
        event_id: str,
        include_attendees: Union[Optional[bool], UnsetType] = UNSET,
        include_expenses: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> GetEvent:
        query = gql("""
            query GetEvent($eventId: uuid!, $includeAttendees: Boolean = false, $includeExpenses: Boolean = false) {
              eetschema_event_by_pk(id: $eventId) {
                ...EventFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }

            fragment EventFields on eetschema_event {
              id
              group_id
              open
              start_date
              closed_by
              signup_deadline
              changed_signup_time
              name
              description
              user {
                id
                name
              }
              created_at
              updated_at
              linked_expenses @include(if: $includeExpenses) {
                ...ExpenseFields
              }
              event_attendees @include(if: $includeAttendees) {
                ...AttendanceFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {
            "eventId": event_id,
            "includeAttendees": include_attendees,
            "includeExpenses": include_expenses,
        }
        response = await self.execute(
            query=query, operation_name="GetEvent", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetEvent.model_validate(data)

    async def all_events_subscription(
        self,
        where: Union[Optional[eetschema_event_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_event_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        include_attendees: Union[Optional[bool], UnsetType] = UNSET,
        include_expenses: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[AllEventsSubscription]:
        query = gql("""
            subscription AllEventsSubscription($where: eetschema_event_bool_exp, $order: [eetschema_event_order_by!], $limit: Int, $includeAttendees: Boolean = false, $includeExpenses: Boolean = false) {
              eetschema_event(where: $where, order_by: $order, limit: $limit) {
                ...EventFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }

            fragment EventFields on eetschema_event {
              id
              group_id
              open
              start_date
              closed_by
              signup_deadline
              changed_signup_time
              name
              description
              user {
                id
                name
              }
              created_at
              updated_at
              linked_expenses @include(if: $includeExpenses) {
                ...ExpenseFields
              }
              event_attendees @include(if: $includeAttendees) {
                ...AttendanceFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {
            "where": where,
            "order": order,
            "limit": limit,
            "includeAttendees": include_attendees,
            "includeExpenses": include_expenses,
        }
        async for data in self.execute_ws(
            query=query,
            operation_name="AllEventsSubscription",
            variables=variables,
            **kwargs,
        ):
            yield AllEventsSubscription.model_validate(data)

    async def get_event_subscription(
        self,
        event_id: str,
        include_attendees: Union[Optional[bool], UnsetType] = UNSET,
        include_expenses: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[GetEventSubscription]:
        query = gql("""
            subscription GetEventSubscription($eventId: uuid!, $includeAttendees: Boolean = false, $includeExpenses: Boolean = false) {
              eetschema_event_by_pk(id: $eventId) {
                ...EventFields
              }
            }

            fragment AttendanceFields on eetschema_event_attendees {
              created_at
              updated_at
              comment
              number_guests
              status
              linked_event {
                id
                name
              }
              user_in_group {
                order
                user {
                  id
                  name
                }
              }
            }

            fragment EventFields on eetschema_event {
              id
              group_id
              open
              start_date
              closed_by
              signup_deadline
              changed_signup_time
              name
              description
              user {
                id
                name
              }
              created_at
              updated_at
              linked_expenses @include(if: $includeExpenses) {
                ...ExpenseFields
              }
              event_attendees @include(if: $includeAttendees) {
                ...AttendanceFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {
            "eventId": event_id,
            "includeAttendees": include_attendees,
            "includeExpenses": include_expenses,
        }
        async for data in self.execute_ws(
            query=query,
            operation_name="GetEventSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GetEventSubscription.model_validate(data)

    async def create_expense(
        self,
        group_id: str,
        payed_by: str,
        data: list[eetschema_expense_distribution_insert_input],
        description: str,
        payed_amount: int,
        payed_at: datetime,
        event_id: Union[Optional[str], UnsetType] = UNSET,
        settlement_expense_id: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> CreateExpense:
        query = gql("""
            mutation CreateExpense($groupId: uuid!, $payedBy: String!, $data: [eetschema_expense_distribution_insert_input!]!, $description: String!, $payedAmount: Int!, $payedAt: timestamptz!, $eventId: uuid, $settlementExpenseId: uuid) {
              insert_eetschema_expense_one(
                object: {description: $description, expense_distributions: {data: $data}, group_id: $groupId, payed_by: $payedBy, payed_amount: $payedAmount, event_id: $eventId, settlement_expense_id: $settlementExpenseId, payed_at: $payedAt}
              ) {
                ...ExpenseFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {
            "groupId": group_id,
            "payedBy": payed_by,
            "data": data,
            "description": description,
            "payedAmount": payed_amount,
            "payedAt": payed_at,
            "eventId": event_id,
            "settlementExpenseId": settlement_expense_id,
        }
        response = await self.execute(
            query=query, operation_name="CreateExpense", variables=variables, **kwargs
        )
        _data = self.get_data(response)
        return CreateExpense.model_validate(_data)

    async def update_expense(
        self, expense_id: str, set_: eetschema_expense_set_input, **kwargs: Any
    ) -> UpdateExpense:
        query = gql("""
            mutation UpdateExpense($expenseId: uuid!, $_set: eetschema_expense_set_input!) {
              update_eetschema_expense(where: {id: {_eq: $expenseId}}, _set: $_set) {
                returning {
                  ...ExpenseFields
                }
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {"expenseId": expense_id, "_set": set_}
        response = await self.execute(
            query=query, operation_name="UpdateExpense", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateExpense.model_validate(data)

    async def update_expense_distribution(
        self,
        expense_id: str,
        objects: list[eetschema_expense_distribution_insert_input],
        **kwargs: Any,
    ) -> UpdateExpenseDistribution:
        query = gql("""
            mutation UpdateExpenseDistribution($expenseId: uuid!, $objects: [eetschema_expense_distribution_insert_input!]!) {
              delete_eetschema_expense_distribution(where: {expense_id: {_eq: $expenseId}}) {
                affected_rows
              }
              insert_eetschema_expense_distribution(objects: $objects) {
                affected_rows
              }
            }
            """)
        variables: dict[str, object] = {"expenseId": expense_id, "objects": objects}
        response = await self.execute(
            query=query,
            operation_name="UpdateExpenseDistribution",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return UpdateExpenseDistribution.model_validate(data)

    async def all_expenses(
        self,
        where: Union[Optional[eetschema_expense_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_expense_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AllExpenses:
        query = gql("""
            query AllExpenses($where: eetschema_expense_bool_exp, $order: [eetschema_expense_order_by!], $limit: Int) {
              eetschema_expense(where: $where, order_by: $order, limit: $limit) {
                ...ExpenseFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        response = await self.execute(
            query=query, operation_name="AllExpenses", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AllExpenses.model_validate(data)

    async def get_expense(self, id: str, **kwargs: Any) -> GetExpense:
        query = gql("""
            query GetExpense($id: uuid!) {
              eetschema_expense_by_pk(id: $id) {
                ...ExpenseFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {"id": id}
        response = await self.execute(
            query=query, operation_name="GetExpense", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetExpense.model_validate(data)

    async def group_total_expense(
        self, group_id: Union[Optional[str], UnsetType] = UNSET, **kwargs: Any
    ) -> GroupTotalExpense:
        query = gql("""
            query GroupTotalExpense($groupId: uuid) {
              eetschema_expense_aggregate(
                where: {group_id: {_eq: $groupId}, deleted: {_eq: false}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
              eetschema_expense_eetlijst_import_aggregate(where: {group_id: {_eq: $groupId}}) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"groupId": group_id}
        response = await self.execute(
            query=query,
            operation_name="GroupTotalExpense",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return GroupTotalExpense.model_validate(data)

    async def all_expenses_subscription(
        self,
        where: Union[Optional[eetschema_expense_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_expense_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[AllExpensesSubscription]:
        query = gql("""
            subscription AllExpensesSubscription($where: eetschema_expense_bool_exp, $order: [eetschema_expense_order_by!], $limit: Int) {
              eetschema_expense(where: $where, order_by: $order, limit: $limit) {
                ...ExpenseFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        async for data in self.execute_ws(
            query=query,
            operation_name="AllExpensesSubscription",
            variables=variables,
            **kwargs,
        ):
            yield AllExpensesSubscription.model_validate(data)

    async def get_expense_subscription(
        self, id: str, **kwargs: Any
    ) -> AsyncIterator[GetExpenseSubscription]:
        query = gql("""
            subscription GetExpenseSubscription($id: uuid!) {
              eetschema_expense_by_pk(id: $id) {
                ...ExpenseFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {"id": id}
        async for data in self.execute_ws(
            query=query,
            operation_name="GetExpenseSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GetExpenseSubscription.model_validate(data)

    async def group_total_expense_subscription(
        self, group_id: Union[Optional[str], UnsetType] = UNSET, **kwargs: Any
    ) -> AsyncIterator[GroupTotalExpenseSubscription]:
        query = gql("""
            subscription GroupTotalExpenseSubscription($groupId: uuid) {
              eetschema_expense_aggregate(
                where: {group_id: {_eq: $groupId}, deleted: {_eq: false}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"groupId": group_id}
        async for data in self.execute_ws(
            query=query,
            operation_name="GroupTotalExpenseSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GroupTotalExpenseSubscription.model_validate(data)

    async def group_total_expense_import_subscription(
        self, group_id: Union[Optional[str], UnsetType] = UNSET, **kwargs: Any
    ) -> AsyncIterator[GroupTotalExpenseImportSubscription]:
        query = gql("""
            subscription GroupTotalExpenseImportSubscription($groupId: uuid) {
              eetschema_expense_eetlijst_import_aggregate(where: {group_id: {_eq: $groupId}}) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"groupId": group_id}
        async for data in self.execute_ws(
            query=query,
            operation_name="GroupTotalExpenseImportSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GroupTotalExpenseImportSubscription.model_validate(data)

    async def create_many_list_items(
        self, items: list[eetschema_list_insert_input], **kwargs: Any
    ) -> CreateManyListItems:
        query = gql("""
            mutation CreateManyListItems($items: [eetschema_list_insert_input!]!) {
              insert_eetschema_list(objects: $items) {
                returning {
                  ...ListItemFields
                }
              }
            }

            fragment ListItemFields on eetschema_list {
              active
              checked
              group_id
              id
              text
              recipe_id
              created_at
              updated_at
            }
            """)
        variables: dict[str, object] = {"items": items}
        response = await self.execute(
            query=query,
            operation_name="CreateManyListItems",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return CreateManyListItems.model_validate(data)

    async def create_list_item(
        self,
        group_id: str,
        text: str,
        active: Union[Optional[bool], UnsetType] = UNSET,
        checked: Union[Optional[bool], UnsetType] = UNSET,
        recipe_id: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> CreateListItem:
        query = gql("""
            mutation CreateListItem($groupId: uuid!, $text: String!, $active: Boolean = true, $checked: Boolean = false, $recipeId: uuid) {
              insert_eetschema_list_one(
                object: {group_id: $groupId, text: $text, active: $active, checked: $checked, recipe_id: $recipeId}
              ) {
                ...ListItemFields
              }
            }

            fragment ListItemFields on eetschema_list {
              active
              checked
              group_id
              id
              text
              recipe_id
              created_at
              updated_at
            }
            """)
        variables: dict[str, object] = {
            "groupId": group_id,
            "text": text,
            "active": active,
            "checked": checked,
            "recipeId": recipe_id,
        }
        response = await self.execute(
            query=query, operation_name="CreateListItem", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CreateListItem.model_validate(data)

    async def update_list_item(
        self, id: str, set_: eetschema_list_set_input, **kwargs: Any
    ) -> UpdateListItem:
        query = gql("""
            mutation UpdateListItem($id: uuid!, $_set: eetschema_list_set_input!) {
              update_eetschema_list_by_pk(pk_columns: {id: $id}, _set: $_set) {
                ...ListItemFields
              }
            }

            fragment ListItemFields on eetschema_list {
              active
              checked
              group_id
              id
              text
              recipe_id
              created_at
              updated_at
            }
            """)
        variables: dict[str, object] = {"id": id, "_set": set_}
        response = await self.execute(
            query=query, operation_name="UpdateListItem", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateListItem.model_validate(data)

    async def get_list_item(self, id: str, **kwargs: Any) -> GetListItem:
        query = gql("""
            query GetListItem($id: uuid!) {
              eetschema_list_by_pk(id: $id) {
                ...ListItemFields
              }
            }

            fragment ListItemFields on eetschema_list {
              active
              checked
              group_id
              id
              text
              recipe_id
              created_at
              updated_at
            }
            """)
        variables: dict[str, object] = {"id": id}
        response = await self.execute(
            query=query, operation_name="GetListItem", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetListItem.model_validate(data)

    async def list_items(
        self,
        where: Union[Optional[eetschema_list_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_list_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> ListItems:
        query = gql("""
            query ListItems($where: eetschema_list_bool_exp, $order: [eetschema_list_order_by!], $limit: Int) {
              eetschema_list(where: $where, order_by: $order, limit: $limit) {
                ...ListItemFields
              }
            }

            fragment ListItemFields on eetschema_list {
              active
              checked
              group_id
              id
              text
              recipe_id
              created_at
              updated_at
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        response = await self.execute(
            query=query, operation_name="ListItems", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ListItems.model_validate(data)

    async def get_list_item_subscription(
        self, id: str, **kwargs: Any
    ) -> AsyncIterator[GetListItemSubscription]:
        query = gql("""
            subscription GetListItemSubscription($id: uuid!) {
              eetschema_list_by_pk(id: $id) {
                ...ListItemFields
              }
            }

            fragment ListItemFields on eetschema_list {
              active
              checked
              group_id
              id
              text
              recipe_id
              created_at
              updated_at
            }
            """)
        variables: dict[str, object] = {"id": id}
        async for data in self.execute_ws(
            query=query,
            operation_name="GetListItemSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GetListItemSubscription.model_validate(data)

    async def list_items_subscription(
        self,
        where: Union[Optional[eetschema_list_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_list_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[ListItemsSubscription]:
        query = gql("""
            subscription ListItemsSubscription($where: eetschema_list_bool_exp, $order: [eetschema_list_order_by!], $limit: Int) {
              eetschema_list(where: $where, order_by: $order, limit: $limit) {
                ...ListItemFields
              }
            }

            fragment ListItemFields on eetschema_list {
              active
              checked
              group_id
              id
              text
              recipe_id
              created_at
              updated_at
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        async for data in self.execute_ws(
            query=query,
            operation_name="ListItemsSubscription",
            variables=variables,
            **kwargs,
        ):
            yield ListItemsSubscription.model_validate(data)

    async def join_group(
        self, group_id: str, user_id: str, invite_id: str, **kwargs: Any
    ) -> JoinGroup:
        query = gql("""
            mutation JoinGroup($groupId: uuid!, $userId: String!, $inviteId: uuid!) {
              joinGroup(group_id: $groupId, user_id: $userId, invite_id: $inviteId) {
                accepted
                error
              }
            }
            """)
        variables: dict[str, object] = {
            "groupId": group_id,
            "userId": user_id,
            "inviteId": invite_id,
        }
        response = await self.execute(
            query=query, operation_name="JoinGroup", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return JoinGroup.model_validate(data)

    async def update_users_in_group(
        self, updates: list[eetschema_users_in_group_updates], **kwargs: Any
    ) -> UpdateUsersInGroup:
        query = gql("""
            mutation UpdateUsersInGroup($updates: [eetschema_users_in_group_updates!]!) {
              update_eetschema_users_in_group_many(updates: $updates) {
                number_users_in_group: affected_rows
                users_in_group: returning {
                  ...UserInGroupFields
                }
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {"updates": updates}
        response = await self.execute(
            query=query,
            operation_name="UpdateUsersInGroup",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return UpdateUsersInGroup.model_validate(data)

    async def update_user_in_group(
        self,
        group_id: str,
        user_id: str,
        set_: eetschema_users_in_group_set_input,
        **kwargs: Any,
    ) -> UpdateUserInGroup:
        query = gql("""
            mutation UpdateUserInGroup($groupId: uuid!, $userId: String!, $_set: eetschema_users_in_group_set_input!) {
              update_eetschema_users_in_group_by_pk(
                _set: $_set
                pk_columns: {group_id: $groupId, user_id: $userId}
              ) {
                ...UserInGroupFields
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {
            "groupId": group_id,
            "userId": user_id,
            "_set": set_,
        }
        response = await self.execute(
            query=query,
            operation_name="UpdateUserInGroup",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return UpdateUserInGroup.model_validate(data)

    async def all_users_in_group(
        self,
        group_id: str,
        where: Union[Optional[eetschema_users_in_group_bool_exp], UnsetType] = UNSET,
        order: Union[
            Optional[list[eetschema_users_in_group_order_by]], UnsetType
        ] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AllUsersInGroup:
        query = gql("""
            query AllUsersInGroup($groupId: uuid!, $where: eetschema_users_in_group_bool_exp, $order: [eetschema_users_in_group_order_by!], $limit: Int) {
              eetschema_group_by_pk(id: $groupId) {
                users_in_groups(where: $where, order_by: $order, limit: $limit) {
                  ...UserInGroupFields
                }
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {
            "groupId": group_id,
            "where": where,
            "order": order,
            "limit": limit,
        }
        response = await self.execute(
            query=query, operation_name="AllUsersInGroup", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AllUsersInGroup.model_validate(data)

    async def get_user_in_group(
        self, group_id: str, user_id: str, **kwargs: Any
    ) -> GetUserInGroup:
        query = gql("""
            query GetUserInGroup($groupId: uuid!, $userId: String!) {
              eetschema_group_by_pk(id: $groupId) {
                users_in_groups(where: {user_id: {_eq: $userId}}) {
                  ...UserInGroupFields
                }
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {"groupId": group_id, "userId": user_id}
        response = await self.execute(
            query=query, operation_name="GetUserInGroup", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetUserInGroup.model_validate(data)

    async def all_users_in_group_subscription(
        self,
        group_id: str,
        where: Union[Optional[eetschema_users_in_group_bool_exp], UnsetType] = UNSET,
        order: Union[
            Optional[list[eetschema_users_in_group_order_by]], UnsetType
        ] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[AllUsersInGroupSubscription]:
        query = gql("""
            subscription AllUsersInGroupSubscription($groupId: uuid!, $where: eetschema_users_in_group_bool_exp, $order: [eetschema_users_in_group_order_by!], $limit: Int) {
              eetschema_group_by_pk(id: $groupId) {
                users_in_groups(where: $where, order_by: $order, limit: $limit) {
                  ...UserInGroupFields
                }
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {
            "groupId": group_id,
            "where": where,
            "order": order,
            "limit": limit,
        }
        async for data in self.execute_ws(
            query=query,
            operation_name="AllUsersInGroupSubscription",
            variables=variables,
            **kwargs,
        ):
            yield AllUsersInGroupSubscription.model_validate(data)

    async def get_user_in_group_subscription(
        self, group_id: str, user_id: str, **kwargs: Any
    ) -> AsyncIterator[GetUserInGroupSubscription]:
        query = gql("""
            subscription GetUserInGroupSubscription($groupId: uuid!, $userId: String!) {
              eetschema_group_by_pk(id: $groupId) {
                users_in_groups(where: {user_id: {_eq: $userId}}) {
                  ...UserInGroupFields
                }
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {"groupId": group_id, "userId": user_id}
        async for data in self.execute_ws(
            query=query,
            operation_name="GetUserInGroupSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GetUserInGroupSubscription.model_validate(data)

    async def create_group(self, name: str, user_id: str, **kwargs: Any) -> CreateGroup:
        query = gql("""
            mutation CreateGroup($name: String!, $userId: String!) {
              group: insert_eetschema_group_one(
                object: {name: $name, users_in_groups: {data: {user_id: $userId}}}
              ) {
                ...GroupFields
              }
            }

            fragment GroupFields on eetschema_group {
              id
              name
              default_close_time
              created_at
              created_at_eetlijst
              statistics_start_date
              statistics_end_date
              invite_uuid
              invite_open
              description
              summary(order_by: {payed_total: desc}) {
                payed_total
                user_id
              }
            }
            """)
        variables: dict[str, object] = {"name": name, "userId": user_id}
        response = await self.execute(
            query=query, operation_name="CreateGroup", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CreateGroup.model_validate(data)

    async def update_group(
        self, group_id: str, set_: eetschema_group_set_input, **kwargs: Any
    ) -> UpdateGroup:
        query = gql("""
            mutation UpdateGroup($groupId: uuid!, $_set: eetschema_group_set_input!) {
              group: update_eetschema_group_by_pk(pk_columns: {id: $groupId}, _set: $_set) {
                ...GroupFields
              }
            }

            fragment GroupFields on eetschema_group {
              id
              name
              default_close_time
              created_at
              created_at_eetlijst
              statistics_start_date
              statistics_end_date
              invite_uuid
              invite_open
              description
              summary(order_by: {payed_total: desc}) {
                payed_total
                user_id
              }
            }
            """)
        variables: dict[str, object] = {"groupId": group_id, "_set": set_}
        response = await self.execute(
            query=query, operation_name="UpdateGroup", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateGroup.model_validate(data)

    async def all_groups(
        self,
        where: Union[Optional[eetschema_users_in_group_bool_exp], UnsetType] = UNSET,
        order: Union[
            Optional[list[eetschema_users_in_group_order_by]], UnsetType
        ] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        include_users: Union[Optional[bool], UnsetType] = UNSET,
        include_inactive_users: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AllGroups:
        query = gql("""
            query AllGroups($where: eetschema_users_in_group_bool_exp, $order: [eetschema_users_in_group_order_by!], $limit: Int, $includeUsers: Boolean = false, $includeInactiveUsers: Boolean = false) {
              eetschema_users_in_group(where: $where, order_by: $order, limit: $limit) {
                group {
                  ...GroupFields
                  users_in_groups(
                    where: {_or: [{active: {_eq: true}}, {active: {_neq: $includeInactiveUsers}}]}
                    order_by: {order: asc}
                  ) @include(if: $includeUsers) {
                    ...UserInGroupFields
                  }
                }
              }
            }

            fragment GroupFields on eetschema_group {
              id
              name
              default_close_time
              created_at
              created_at_eetlijst
              statistics_start_date
              statistics_end_date
              invite_uuid
              invite_open
              description
              summary(order_by: {payed_total: desc}) {
                payed_total
                user_id
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {
            "where": where,
            "order": order,
            "limit": limit,
            "includeUsers": include_users,
            "includeInactiveUsers": include_inactive_users,
        }
        response = await self.execute(
            query=query, operation_name="AllGroups", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AllGroups.model_validate(data)

    async def get_group(
        self,
        group_id: str,
        include_users: Union[Optional[bool], UnsetType] = UNSET,
        include_inactive_users: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> GetGroup:
        query = gql("""
            query GetGroup($groupId: uuid!, $includeUsers: Boolean = false, $includeInactiveUsers: Boolean = false) {
              eetschema_group_by_pk(id: $groupId) {
                ...GroupFields
                users_in_groups(
                  where: {_or: [{active: {_eq: true}}, {active: {_neq: $includeInactiveUsers}}]}
                  order_by: {order: asc}
                ) @include(if: $includeUsers) {
                  ...UserInGroupFields
                }
              }
            }

            fragment GroupFields on eetschema_group {
              id
              name
              default_close_time
              created_at
              created_at_eetlijst
              statistics_start_date
              statistics_end_date
              invite_uuid
              invite_open
              description
              summary(order_by: {payed_total: desc}) {
                payed_total
                user_id
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {
            "groupId": group_id,
            "includeUsers": include_users,
            "includeInactiveUsers": include_inactive_users,
        }
        response = await self.execute(
            query=query, operation_name="GetGroup", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetGroup.model_validate(data)

    async def all_groups_subscription(
        self,
        where: Union[Optional[eetschema_users_in_group_bool_exp], UnsetType] = UNSET,
        order: Union[
            Optional[list[eetschema_users_in_group_order_by]], UnsetType
        ] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        include_users: Union[Optional[bool], UnsetType] = UNSET,
        include_inactive_users: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[AllGroupsSubscription]:
        query = gql("""
            subscription AllGroupsSubscription($where: eetschema_users_in_group_bool_exp, $order: [eetschema_users_in_group_order_by!], $limit: Int, $includeUsers: Boolean = false, $includeInactiveUsers: Boolean = false) {
              eetschema_users_in_group(where: $where, order_by: $order, limit: $limit) {
                group {
                  ...GroupFields
                  users_in_groups(
                    where: {_or: [{active: {_eq: true}}, {active: {_neq: $includeInactiveUsers}}]}
                    order_by: {order: asc}
                  ) @include(if: $includeUsers) {
                    ...UserInGroupFields
                  }
                }
              }
            }

            fragment GroupFields on eetschema_group {
              id
              name
              default_close_time
              created_at
              created_at_eetlijst
              statistics_start_date
              statistics_end_date
              invite_uuid
              invite_open
              description
              summary(order_by: {payed_total: desc}) {
                payed_total
                user_id
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {
            "where": where,
            "order": order,
            "limit": limit,
            "includeUsers": include_users,
            "includeInactiveUsers": include_inactive_users,
        }
        async for data in self.execute_ws(
            query=query,
            operation_name="AllGroupsSubscription",
            variables=variables,
            **kwargs,
        ):
            yield AllGroupsSubscription.model_validate(data)

    async def get_group_subscription(
        self,
        group_id: str,
        include_users: Union[Optional[bool], UnsetType] = UNSET,
        include_inactive_users: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[GetGroupSubscription]:
        query = gql("""
            subscription GetGroupSubscription($groupId: uuid!, $includeUsers: Boolean = false, $includeInactiveUsers: Boolean = false) {
              eetschema_group_by_pk(id: $groupId) {
                ...GroupFields
                users_in_groups(
                  where: {_or: [{active: {_eq: true}}, {active: {_neq: $includeInactiveUsers}}]}
                  order_by: {order: asc}
                ) @include(if: $includeUsers) {
                  ...UserInGroupFields
                }
              }
            }

            fragment GroupFields on eetschema_group {
              id
              name
              default_close_time
              created_at
              created_at_eetlijst
              statistics_start_date
              statistics_end_date
              invite_uuid
              invite_open
              description
              summary(order_by: {payed_total: desc}) {
                payed_total
                user_id
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }

            fragment UserInGroupFields on eetschema_users_in_group {
              active
              order
              start_holliday
              end_holliday
              monday
              tuesday
              wednesday
              thursday
              friday
              saturday
              sunday
              user {
                ...UserFields
              }
            }
            """)
        variables: dict[str, object] = {
            "groupId": group_id,
            "includeUsers": include_users,
            "includeInactiveUsers": include_inactive_users,
        }
        async for data in self.execute_ws(
            query=query,
            operation_name="GetGroupSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GetGroupSubscription.model_validate(data)

    async def create_settlement(self, group_id: str, **kwargs: Any) -> CreateSettlement:
        query = gql("""
            mutation CreateSettlement($groupId: uuid!) {
              settlement: insert_eetschema_settlements_one(object: {group_id: $groupId}) {
                ...SettlementFields
              }
            }

            fragment SettlementFields on eetschema_settlements {
              id
              group_id
              created_at
              updated_at
              created_by: user {
                id
                name
              }
              expenses_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: true}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
              adjustments_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: false}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"groupId": group_id}
        response = await self.execute(
            query=query,
            operation_name="CreateSettlement",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return CreateSettlement.model_validate(data)

    async def settle_unsettled_expenses(
        self, settlement_id: str, where: eetschema_expense_bool_exp, **kwargs: Any
    ) -> SettleUnsettledExpenses:
        query = gql("""
            mutation SettleUnsettledExpenses($settlementId: uuid!, $where: eetschema_expense_bool_exp!) {
              update_eetschema_expense(where: $where, _set: {settled_id: $settlementId}) {
                number_expenses: affected_rows
                expenses: returning {
                  ...ExpenseFields
                }
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {"settlementId": settlement_id, "where": where}
        response = await self.execute(
            query=query,
            operation_name="SettleUnsettledExpenses",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return SettleUnsettledExpenses.model_validate(data)

    async def all_settlements(
        self,
        where: Union[Optional[eetschema_settlements_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_settlements_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AllSettlements:
        query = gql("""
            query AllSettlements($where: eetschema_settlements_bool_exp, $order: [eetschema_settlements_order_by!], $limit: Int) {
              eetschema_settlements(where: $where, order_by: $order, limit: $limit) {
                ...SettlementFields
              }
            }

            fragment SettlementFields on eetschema_settlements {
              id
              group_id
              created_at
              updated_at
              created_by: user {
                id
                name
              }
              expenses_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: true}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
              adjustments_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: false}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        response = await self.execute(
            query=query, operation_name="AllSettlements", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AllSettlements.model_validate(data)

    async def settlement_expenses(
        self,
        where: Union[Optional[eetschema_expense_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_expense_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> SettlementExpenses:
        query = gql("""
            query SettlementExpenses($where: eetschema_expense_bool_exp, $order: [eetschema_expense_order_by!], $limit: Int) {
              eetschema_expense(where: $where, order_by: $order, limit: $limit) {
                ...ExpenseFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        response = await self.execute(
            query=query,
            operation_name="SettlementExpenses",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return SettlementExpenses.model_validate(data)

    async def get_settlement(self, id: str, **kwargs: Any) -> GetSettlement:
        query = gql("""
            query GetSettlement($id: uuid!) {
              eetschema_settlements_by_pk(id: $id) {
                ...SettlementFields
              }
            }

            fragment SettlementFields on eetschema_settlements {
              id
              group_id
              created_at
              updated_at
              created_by: user {
                id
                name
              }
              expenses_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: true}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
              adjustments_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: false}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"id": id}
        response = await self.execute(
            query=query, operation_name="GetSettlement", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetSettlement.model_validate(data)

    async def all_settlements_subscription(
        self,
        where: Union[Optional[eetschema_settlements_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_settlements_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[AllSettlementsSubscription]:
        query = gql("""
            subscription AllSettlementsSubscription($where: eetschema_settlements_bool_exp, $order: [eetschema_settlements_order_by!], $limit: Int) {
              eetschema_settlements(where: $where, order_by: $order, limit: $limit) {
                ...SettlementFields
              }
            }

            fragment SettlementFields on eetschema_settlements {
              id
              group_id
              created_at
              updated_at
              created_by: user {
                id
                name
              }
              expenses_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: true}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
              adjustments_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: false}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        async for data in self.execute_ws(
            query=query,
            operation_name="AllSettlementsSubscription",
            variables=variables,
            **kwargs,
        ):
            yield AllSettlementsSubscription.model_validate(data)

    async def settlement_expenses_subscription(
        self,
        where: Union[Optional[eetschema_expense_bool_exp], UnsetType] = UNSET,
        order: Union[Optional[list[eetschema_expense_order_by]], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any,
    ) -> AsyncIterator[SettlementExpensesSubscription]:
        query = gql("""
            subscription SettlementExpensesSubscription($where: eetschema_expense_bool_exp, $order: [eetschema_expense_order_by!], $limit: Int) {
              eetschema_expense(where: $where, order_by: $order, limit: $limit) {
                ...ExpenseFields
              }
            }

            fragment ExpenseFields on eetschema_expense {
              id
              event_id
              settled_id
              description
              payed_amount
              deleted
              settlement_expense_id
              expense_distributions {
                id
                count
                payed_amount
                user {
                  id
                  name
                }
              }
              payed_at
              payed_by: payed_by_user {
                id
                name
              }
              updated_at
              updated_by: updatedByUser {
                id
                name
              }
            }
            """)
        variables: dict[str, object] = {"where": where, "order": order, "limit": limit}
        async for data in self.execute_ws(
            query=query,
            operation_name="SettlementExpensesSubscription",
            variables=variables,
            **kwargs,
        ):
            yield SettlementExpensesSubscription.model_validate(data)

    async def get_settlement_subscription(
        self, id: str, **kwargs: Any
    ) -> AsyncIterator[GetSettlementSubscription]:
        query = gql("""
            subscription GetSettlementSubscription($id: uuid!) {
              eetschema_settlements_by_pk(id: $id) {
                ...SettlementFields
              }
            }

            fragment SettlementFields on eetschema_settlements {
              id
              group_id
              created_at
              updated_at
              created_by: user {
                id
                name
              }
              expenses_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: true}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
              adjustments_total: expenses_aggregate(
                where: {settlement_expense_id: {_is_null: false}}
              ) {
                aggregate {
                  sum {
                    payed_amount
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"id": id}
        async for data in self.execute_ws(
            query=query,
            operation_name="GetSettlementSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GetSettlementSubscription.model_validate(data)

    async def remove_account(
        self,
        user_id: str,
        reason_to_remove_account_text: str,
        reason_to_remove_account_selection: Union[
            Optional[list[str]], UnsetType
        ] = UNSET,
        reason_to_remove_account_selection_all_options: Union[
            Optional[list[str]], UnsetType
        ] = UNSET,
        **kwargs: Any,
    ) -> RemoveAccount:
        query = gql("""
            mutation RemoveAccount($user_id: String!, $reason_to_remove_account_selection: [String!] = "", $reason_to_remove_account_selection_all_options: [String!] = "", $reason_to_remove_account_text: String! = "") {
              update_eetschema_user_by_pk(
                pk_columns: {id: $user_id}
                _set: {reason_to_remove_account_selection: $reason_to_remove_account_selection, reason_to_remove_account_selection_all_options: $reason_to_remove_account_selection_all_options, reason_to_remove_account_text: $reason_to_remove_account_text}
              ) {
                reason_to_remove_account_text
                reason_to_remove_account_selection
                reason_to_remove_account_selection_all_options
              }
            }
            """)
        variables: dict[str, object] = {
            "user_id": user_id,
            "reason_to_remove_account_selection": reason_to_remove_account_selection,
            "reason_to_remove_account_selection_all_options": reason_to_remove_account_selection_all_options,
            "reason_to_remove_account_text": reason_to_remove_account_text,
        }
        response = await self.execute(
            query=query, operation_name="RemoveAccount", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return RemoveAccount.model_validate(data)

    async def update_user(
        self, user_id: str, set_: eetschema_user_set_input, **kwargs: Any
    ) -> UpdateUser:
        query = gql("""
            mutation UpdateUser($userId: String!, $_set: eetschema_user_set_input!) {
              update_eetschema_user_by_pk(pk_columns: {id: $userId}, _set: $_set) {
                ...UserFields
              }
            }

            fragment UserFields on eetschema_user {
              id
              origin
              name
              email
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              wants_to_recieve_notifications
              funnel_lead
              cook_points_imports {
                group_id
                cook_points
                allowed_to_edit
              }
            }
            """)
        variables: dict[str, object] = {"userId": user_id, "_set": set_}
        response = await self.execute(
            query=query, operation_name="UpdateUser", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateUser.model_validate(data)

    async def get_user(self, user_id: str, **kwargs: Any) -> GetUser:
        query = gql("""
            query GetUser($userId: String!) {
              eetschema_user_private(where: {id: {_eq: $userId}}) {
                ...UserFieldsPrivate
              }
            }

            fragment UserFieldsPrivate on eetschema_user_private {
              id
              active
              origin
              last_seen
              name
              email
              address
              phone_nr
              bank_account
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              default_landingpage
              wants_to_recieve_notifications
              is_color_blind
              created_at
              updated_at
            }
            """)
        variables: dict[str, object] = {"userId": user_id}
        response = await self.execute(
            query=query, operation_name="GetUser", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetUser.model_validate(data)

    async def get_user_subscription(
        self, user_id: str, **kwargs: Any
    ) -> AsyncIterator[GetUserSubscription]:
        query = gql("""
            subscription GetUserSubscription($userId: String!) {
              eetschema_user_private(where: {id: {_eq: $userId}}) {
                ...UserFieldsPrivate
              }
            }

            fragment UserFieldsPrivate on eetschema_user_private {
              id
              active
              origin
              last_seen
              name
              email
              address
              phone_nr
              bank_account
              allergies
              birthday
              profile_image
              order_of_buttom_bar
              default_landingpage
              wants_to_recieve_notifications
              is_color_blind
              created_at
              updated_at
            }
            """)
        variables: dict[str, object] = {"userId": user_id}
        async for data in self.execute_ws(
            query=query,
            operation_name="GetUserSubscription",
            variables=variables,
            **kwargs,
        ):
            yield GetUserSubscription.model_validate(data)
