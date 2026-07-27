from dataclasses import dataclass
from datetime import datetime

from eetlijst_py.generated import GraphQlClient, order_by
from eetlijst_py.generated.input_types import (
    eetschema_event_bool_exp,
    eetschema_event_order_by,
    eetschema_event_set_input,
    uuid_comparison_exp,
)

from eetlijst_py.services.event_attendance import EventAttendance

from eetlijst_py.utils.datetime import current_datetime, format_date

from .transformers import (
    transform_automatic_events,
    transform_event,
    transform_update_event,
)


@dataclass
class Events:
    _client: GraphQlClient
    attendance: EventAttendance

    async def populate_dinners(self, group_id: str, date: datetime | str):
        result = await self._client.automatic_events(
            group_id,
            format_date(date),
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
        )
        return transform_event(result.eetschema_event_by_pk)

    async def all(
        self,
        group_id: str,
        where: eetschema_event_bool_exp | None = None,
        order: list[eetschema_event_order_by] | None = None,
        limit: int | None = None,
        include_attendees: bool = False,
        include_expenses: bool = False,
    ):
        if where is not None:
            where_data = where.model_copy(
                update={"group_id": uuid_comparison_exp(_eq=group_id)}
            )
        else:
            where_data = eetschema_event_bool_exp(
                group_id=uuid_comparison_exp(_eq=group_id)
            )

        order_data = order
        if order is None:
            order_data = [eetschema_event_order_by(start_date=order_by.asc)]

        result = await self._client.all_events(
            where_data,
            order_data,
            limit,
            include_attendees,
            include_expenses,
        )
        return [transform_event(event) for event in result.eetschema_event]

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
