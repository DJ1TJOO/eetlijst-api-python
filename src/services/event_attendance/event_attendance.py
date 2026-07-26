from dataclasses import dataclass

from src.generated import GraphQlClient
from src.generated.base_model import UNSET, UnsetType
from src.generated.enums import AttendanceStatus
from src.generated.input_types import (
    eetschema_event_attendees_bool_exp,
    eetschema_event_attendees_insert_input,
    eetschema_event_attendees_order_by,
    eetschema_event_attendees_set_input,
)

from .transformers import (
    transform_attendance,
    transform_update_attendance,
    transform_update_many_attendance,
)


class EventAttendceAttend(eetschema_event_attendees_insert_input):
    user_id: str
    event_id: str
    status: AttendanceStatus


class EventAttendceUpdate(eetschema_event_attendees_set_input):
    user_id: str
    event_id: str


@dataclass
class EventAttendance:
    _client: GraphQlClient

    async def get(
        self,
        event_id: str,
        user_id: str,
    ):
        result = await self._client.get_attendance(event_id, user_id)
        return transform_attendance(result.eetschema_event_attendees_by_pk)

    async def all(
        self,
        where: eetschema_event_attendees_bool_exp | UnsetType | None = UNSET,
        order: list[eetschema_event_attendees_order_by] | UnsetType | None = UNSET,
        limit: int | UnsetType | None = UNSET,
    ):
        result = await self._client.all_attendances(where, order, limit)
        return [
            transform_attendance(attendee)
            for attendee in result.eetschema_event_attendees
        ]

    async def attend(self, data: EventAttendceAttend):
        return await self.update_many([data])

    async def update(self, data: EventAttendceUpdate):
        result = await self._client.update_attendance(data.event_id, data.user_id, data)
        return transform_update_attendance(result)

    async def update_many(self, data: list[eetschema_event_attendees_insert_input]):
        result = await self._client.update_many_attendance(data)
        return transform_update_many_attendance(result)

    async def comment(self, user_id: str, event_id: str, comment: str | None):
        return await self.update(
            EventAttendceUpdate(
                user_id=user_id,
                event_id=event_id,
                comment=comment,
            )
        )

    async def status(
        self, user_id: str, event_id: str, status: AttendanceStatus | None
    ):
        return await self.update(
            EventAttendceUpdate(
                user_id=user_id,
                event_id=event_id,
                status=status,
                user_changed_status=True,
            )
        )

    async def guests(self, user_id: str, event_id: str, guests: int | None):
        return await self.update(
            EventAttendceUpdate(
                user_id=user_id,
                event_id=event_id,
                number_guests=guests,
            )
        )
