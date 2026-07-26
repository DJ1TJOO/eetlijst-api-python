from typing import Optional

from .base_model import BaseModel
from .fragments import EventFields


class GetEvent(BaseModel):
    eetschema_event_by_pk: Optional["GetEventEetschemaEventByPk"]


class GetEventEetschemaEventByPk(EventFields):
    pass


GetEvent.model_rebuild()
