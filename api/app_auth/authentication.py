from datetime import datetime
import time

import jwt

from core.configs.base import SECRET_KEY, JWT_EXPIRED_INTERVAL


def make_token(user):
    expired_at = time.mktime((datetime.now() + JWT_EXPIRED_INTERVAL).timetuple())
    data = {
        'id': user.id,
        'user_name': user.user_name,
        'user_email': user.user_email,
        'is_active': user.is_active,
        'exp': int(expired_at)
    }
    encoded = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return encoded


def autheticate(token):
    jwt.decode(token, SECRET_KEY, algorithms='HS256')
