from typing import Optional

from .base_model import BaseModel
from .fragments import EventFields


class UpdateEvent(BaseModel):
    update_eetschema_event_by_pk: Optional["UpdateEventUpdateEetschemaEventByPk"]


class UpdateEventUpdateEetschemaEventByPk(EventFields):
    pass


UpdateEvent.model_rebuild()
