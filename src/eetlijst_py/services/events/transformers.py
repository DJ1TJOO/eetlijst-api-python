from typing import Optional

from eetlijst_py.generated.automatic_events import (
    AutomaticEvents,
    AutomaticEventsQueryTodaysEvents,
)
from eetlijst_py.generated.fragments import EventFields
from eetlijst_py.generated.update_event import UpdateEvent

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.event_attendance.transformers import transform_attendance

from .types import Event


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
