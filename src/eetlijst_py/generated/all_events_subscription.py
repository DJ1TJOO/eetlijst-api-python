from .base_model import BaseModel
from .fragments import EventFields


class AllEventsSubscription(BaseModel):
    eetschema_event: list["AllEventsSubscriptionEetschemaEvent"]


class AllEventsSubscriptionEetschemaEvent(EventFields):
    pass


AllEventsSubscription.model_rebuild()
