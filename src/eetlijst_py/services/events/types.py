"""Events service type exports."""

from datetime import datetime

from eetlijst_py.generated.all_events import AllEventsEetschemaEvent
from eetlijst_py.generated.automatic_events import AutomaticEventsQueryTodaysEvents
from eetlijst_py.generated.base_model import BaseModel
from eetlijst_py.generated.fragments import (
    EventFields,
    EventFieldsEventAttendees,
    EventFieldsLinkedExpenses,
    EventFieldsUser,
)
from eetlijst_py.generated.get_event import GetEventEetschemaEventByPk
from eetlijst_py.generated.input_types import (
    eetschema_event_bool_exp as _eetschema_event_bool_exp,
)
from eetlijst_py.generated.input_types import (
    eetschema_event_order_by as _eetschema_event_order_by,
)
from eetlijst_py.generated.input_types import (
    eetschema_event_set_input as _eetschema_event_set_input,
)
from eetlijst_py.generated.update_event import UpdateEventUpdateEetschemaEventByPk

from eetlijst_py.services.event_attendance.transformers import Attendance


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


WhereEvent = _eetschema_event_bool_exp
OrderEvent = _eetschema_event_order_by
UpdateEvent = _eetschema_event_set_input

__all__ = [
    "Event",
    "EventFields",
    "EventFieldsEventAttendees",
    "EventFieldsLinkedExpenses",
    "EventFieldsUser",
    "AllEventsEetschemaEvent",
    "GetEventEetschemaEventByPk",
    "UpdateEventUpdateEetschemaEventByPk",
    "AutomaticEventsQueryTodaysEvents",
    "WhereEvent",
    "OrderEvent",
    "UpdateEvent",
]
