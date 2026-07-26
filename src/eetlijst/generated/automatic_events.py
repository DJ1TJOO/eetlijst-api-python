from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class AutomaticEvents(BaseModel):
    query_todays_events: Optional["AutomaticEventsQueryTodaysEvents"] = Field(
        alias="queryTodaysEvents"
    )


class AutomaticEventsQueryTodaysEvents(BaseModel):
    id: Optional[str]


AutomaticEvents.model_rebuild()
