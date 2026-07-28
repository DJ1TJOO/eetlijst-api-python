from datetime import datetime
from typing import Optional

from .base_model import BaseModel


class GetEventStatisticsSubscription(BaseModel):
    eetschema_event_statistics: list[
        "GetEventStatisticsSubscriptionEetschemaEventStatistics"
    ]


class GetEventStatisticsSubscriptionEetschemaEventStatistics(BaseModel):
    event_id: str
    group_id: str
    user_id: str
    status: str
    number_guests: int
    total_number_of_eaters: int
    event_start_date: Optional[datetime]


GetEventStatisticsSubscription.model_rebuild()
