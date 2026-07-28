from dataclasses import dataclass

from eetlijst_py.generated.base_model import UNSET, UnsetType

from eetlijst_py.services.base import BaseService
from eetlijst_py.services.event_attendance.types import (
    AttendEvent,
    CreateEventAttendee,
    OrderEventAttendee,
    UpdateAttendance,
    WhereEventAttendee,
)

from .transformers import (
    transform_attendance,
    transform_update_attendance,
    transform_update_many_attendance,
)


@dataclass
class EventAttendance(BaseService):

    async def get(
        self,
        event_id: str,
        user_id: str,
    ):
        result = await self._client.get_attendance(
            event_id,
            user_id,
            headers=self._get_headers(),
        )
        return transform_attendance(result.eetschema_event_attendees_by_pk)

    async def get_subscription(self, event_id: str, user_id: str):
        async for result in self._client.get_attendance_subscription(
            event_id,
            user_id,
            headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_event_attendees_by_pk:
                yield transform_attendance(result.eetschema_event_attendees_by_pk)

    async def all(
        self,
        where: WhereEventAttendee | UnsetType | None = UNSET,
        order: list[OrderEventAttendee] | UnsetType | None = UNSET,
        limit: int | UnsetType | None = UNSET,
    ):
        result = await self._client.all_attendances(
            where,
            order,
            limit,
            headers=self._get_headers(),
        )
        return [
            transform_attendance(attendee)
            for attendee in result.eetschema_event_attendees
        ]

    async def all_subscription(
        self,
        where: WhereEventAttendee | UnsetType | None = UNSET,
        order: list[OrderEventAttendee] | UnsetType | None = UNSET,
        limit: int | UnsetType | None = UNSET,
    ):
        async for result in self._client.all_attendances_subscription(
            where,
            order,
            limit,
            headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_event_attendees:
                yield [
                    transform_attendance(attendee)
                    for attendee in result.eetschema_event_attendees
                ]

    async def attend(self, data: AttendEvent):
        return await self.update_many([data])

    async def update(self, data: UpdateAttendance):
        result = await self._client.update_attendance(
            data.event_id,
            data.user_id,
            data,
            headers=self._get_headers(),
        )
        return transform_update_attendance(result)

    async def update_many(self, data: list[CreateEventAttendee]):
        result = await self._client.update_many_attendance(
            data,
            headers=self._get_headers(),
        )
        return transform_update_many_attendance(result)

    async def comment(self, user_id: str, event_id: str, comment: str | None):
        return await self.update(
            UpdateAttendance(
                user_id=user_id,
                event_id=event_id,
                comment=comment,
            )
        )

    async def status(self, user_id: str, event_id: str, status: str | None):
        return await self.update(
            UpdateAttendance(
                user_id=user_id,
                event_id=event_id,
                status=status,
                user_changed_status=True,
            )
        )

    async def guests(self, user_id: str, event_id: str, guests: int | None):
        return await self.update(
            UpdateAttendance(
                user_id=user_id,
                event_id=event_id,
                number_guests=guests,
            )
        )
