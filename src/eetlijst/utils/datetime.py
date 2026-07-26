from datetime import datetime


def current_datetime() -> datetime:
    return datetime.now()


def format_date(date: datetime | str) -> str:
    if isinstance(date, str):
        return date

    return date.strftime("%Y-%m-%d:%H:%M:%S")


def coerce_datetime(date: datetime | str | None) -> datetime | None:
    if date is None:
        return None

    if isinstance(date, datetime):
        return date

    try:
        return datetime.fromisoformat(date)
    except ValueError:
        return datetime.strptime(date, "%Y-%m-%d:%H:%M:%S")
