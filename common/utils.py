from datetime import date, datetime

from pytz import timezone

from core.config import DEFAULT_TIMEZONE

tz = timezone(DEFAULT_TIMEZONE)


def encode(obj):
    if isinstance(obj, datetime):
        return obj.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    else:
        return str(obj)
