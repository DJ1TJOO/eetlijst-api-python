from typing import Optional

from .base_model import BaseModel
from .fragments import EventFields


class GetEventSubscription(BaseModel):
    eetschema_event_by_pk: Optional["GetEventSubscriptionEetschemaEventByPk"]


class GetEventSubscriptionEetschemaEventByPk(EventFields):
    pass


GetEventSubscription.model_rebuild()
