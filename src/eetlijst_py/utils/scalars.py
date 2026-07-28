import datetime


def serialize_datetime(dt: datetime.datetime) -> str:
    return dt.isoformat()
