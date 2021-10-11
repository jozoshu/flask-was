from datetime import date, datetime

import bcrypt
from pytz import timezone

from core.configs.base import DEFAULT_TIMEZONE

tz = timezone(DEFAULT_TIMEZONE)


def encode(obj: object) -> str:
    if isinstance(obj, datetime):
        return obj.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    else:
        return str(obj)


def hash_password(password: str) -> str:
    pw = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
    return pw.decode('UTF-8')


def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('UTF-8'), hashed_password.encode('UTF-8'))
