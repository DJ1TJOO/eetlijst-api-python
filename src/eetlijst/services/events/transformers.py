from datetime import datetime
from typing import Optional

from eetlijst.generated.automatic_events import (
    AutomaticEvents,
    AutomaticEventsQueryTodaysEvents,
)
from eetlijst.generated.base_model import BaseModel
from eetlijst.generated.fragments import (
    EventFields,
    EventFieldsLinkedExpenses,
    EventFieldsUser,
)
from eetlijst.generated.update_event import UpdateEvent

from eetlijst.exceptions import EetlijstException

from eetlijst.services.event_attendance.transformers import (
    Attendance,
    transform_attendance,
)


class Event(BaseModel):
    id: str
    group_id: str
    open: bool
    start_date: datetime
    closed_by: str | None
    signup_deadline: datetime | None
    changed_signup_time: bool
    name: str
    description: str | None
    user: EventFieldsUser | None
    created_at: datetime | None
    updated_at: datetime | None
    expenses: list[EventFieldsLinkedExpenses] | None = None
    attendees: list[Attendance] | None = None


def transform_automatic_events(
    events: AutomaticEvents,
) -> AutomaticEventsQueryTodaysEvents:
    if not events or not events.query_todays_events:
        raise EetlijstException("Failed to populate dinners")

    return events.query_todays_events


def transform_event(event: Optional[EventFields]) -> Event:
    if not event:
        raise EetlijstException("Event not found")

    data = event.model_dump(exclude={"linked_expenses", "event_attendees"})
    data["expenses"] = event.linked_expenses  # TODO: add transform_expense
    data["attendees"] = [
        transform_attendance(attendee) for attendee in (event.event_attendees or [])
    ]

    return Event(**data)


def transform_update_event(event: UpdateEvent) -> Event:
    if not event or not event.update_eetschema_event_by_pk:
        raise EetlijstException("Failed to update event")

    return transform_event(event.update_eetschema_event_by_pk)
