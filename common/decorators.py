from functools import wraps
import json
import logging

from flask import request, Response
import jwt

from api.app_auth.authentication import autheticate
from .exception import APIException
from .response import APIResponse
from .response.client_error import Http4XX
from .response.formats import exception, error

logger = logging.getLogger('flast.request')


def exception_format(func):
    """예외 처리하여 Response"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except APIException as ae:
            logger.error(f'{func.__qualname__} - {ae}')
            return Response(
                response=json.dumps(exception(ae)),
                status=ae.status,
                mimetype='application/json'
            )
        except Exception as e:
            logger.error(f'{func.__qualname__} - {e}')
            return Response(
                response=json.dumps(error(e)),
                status=500,
                mimetype='application/json'
            )
    return wrapper


def login_required(func):
    """JWT 토큰 검증"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        try:
            autheticate(token)
        except jwt.DecodeError:
            return APIResponse(Http4XX.INVALID_TOKEN)
        except jwt.ExpiredSignatureError:
            return APIResponse(Http4XX.EXPIRED_TOKEN)
        return func(*args, **kwargs)
    return wrapper
