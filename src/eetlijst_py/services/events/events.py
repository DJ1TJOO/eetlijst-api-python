from dataclasses import dataclass
from datetime import datetime

from eetlijst_py.generated import order_by
from eetlijst_py.generated.input_types import (
    eetschema_event_bool_exp,
    eetschema_event_order_by,
    eetschema_event_set_input,
    uuid_comparison_exp,
)

from eetlijst_py.services.base import BaseService
from eetlijst_py.services.event_attendance import EventAttendance

from eetlijst_py.utils.datetime import current_datetime, format_date
from eetlijst_py.utils.params import build_where, default_order

from .transformers import (
    transform_automatic_events,
    transform_event,
    transform_update_event,
)


@dataclass
class Events(BaseService):
    attendance: EventAttendance

    async def populate_dinners(self, group_id: str, date: datetime | str):
        result = await self._client.automatic_events(
            group_id,
            format_date(date),
            headers=self._get_headers(),
        )
        return transform_automatic_events(result)

    async def get(
        self,
        event_id: str,
        include_attendees: bool = False,
        include_expenses: bool = False,
    ):
        result = await self._client.get_event(
            event_id,
            include_attendees,
            include_expenses,
            headers=self._get_headers(),
        )
        return transform_event(result.eetschema_event_by_pk)

    async def get_subscription(
        self,
        event_id: str,
        include_attendees: bool = False,
        include_expenses: bool = False,
    ):
        async for result in self._client.get_event_subscription(
            event_id,
            include_attendees,
            include_expenses,
            headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_event_by_pk:
                yield transform_event(result.eetschema_event_by_pk)

    async def all(
        self,
        group_id: str,
        where: eetschema_event_bool_exp | None = None,
        order: list[eetschema_event_order_by] | None = None,
        limit: int | None = None,
        include_attendees: bool = False,
        include_expenses: bool = False,
    ):
        where_data = build_where(
            eetschema_event_bool_exp,
            where,
            group_id=uuid_comparison_exp(_eq=group_id),
        )
        order_data = default_order(
            order,
            eetschema_event_order_by(start_date=order_by.asc),
        )

        result = await self._client.all_events(
            where_data,
            order_data,
            limit,
            include_attendees,
            include_expenses,
            headers=self._get_headers(),
        )
        return [transform_event(event) for event in result.eetschema_event]

    async def all_subscription(
        self,
        group_id: str,
        where: eetschema_event_bool_exp | None = None,
        order: list[eetschema_event_order_by] | None = None,
        limit: int | None = None,
        include_attendees: bool = False,
        include_expenses: bool = False,
    ):
        where_data = build_where(
            eetschema_event_bool_exp,
            where,
            group_id=uuid_comparison_exp(_eq=group_id),
        )
        order_data = default_order(
            order,
            eetschema_event_order_by(start_date=order_by.asc),
        )

        async for result in self._client.all_events_subscription(
            where_data,
            order_data,
            limit,
            include_attendees,
            include_expenses,
            headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_event:
                yield [transform_event(event) for event in result.eetschema_event]

    async def update(
        self,
        event_id: str,
        data: eetschema_event_set_input,
        include_attendees: bool = False,
        include_expenses: bool = False,
    ):
        result = await self._client.update_event(
            event_id,
            data,
            include_attendees,
            include_expenses,
            headers=self._get_headers(),
        )
        return transform_update_event(result)

    async def close(
        self,
        event_id: str,
        closed_by: str,
        include_attendees: bool = False,
        include_expenses: bool = False,
    ):
        return await self.update(
            event_id,
            eetschema_event_set_input(
                open=False,
                changed_signup_time=True,
                closed_by=closed_by,
                signup_deadline=current_datetime(),
            ),
            include_attendees,
            include_expenses,
        )

    async def open(
        self,
        event_id: str,
        include_attendees: bool = False,
        include_expenses: bool = False,
    ):
        return await self.update(
            event_id,
            eetschema_event_set_input(
                open=True,
                changed_signup_time=True,
                signup_deadline=current_datetime(),
            ),
            include_attendees,
            include_expenses,
        )

    async def close_at(
        self,
        event_id: str,
        closed_by: str,
        signup_deadline: datetime,
        include_attendees: bool = False,
        include_expenses: bool = False,
    ):
        return await self.update(
            event_id,
            eetschema_event_set_input(
                open=False,
                changed_signup_time=True,
                closed_by=closed_by,
                signup_deadline=signup_deadline,
            ),
            include_attendees,
            include_expenses,
        )
