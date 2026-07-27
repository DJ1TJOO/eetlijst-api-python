from .base_model import BaseModel
from .fragments import EventFields


class AllEvents(BaseModel):
    eetschema_event: list["AllEventsEetschemaEvent"]


class AllEventsEetschemaEvent(EventFields):
    pass


AllEvents.model_rebuild()
