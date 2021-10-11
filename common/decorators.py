from functools import wraps
import json

from flask import request, Response
import jwt

from core.configs.base import SECRET_KEY
from common.exceptions import APIException
from common.response import exception, error, APIResponse


def send_format(func):
    """Response 기본 형태"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except APIException as ae:
            return Response(
                response=json.dumps(exception(ae)),
                status=ae.status,
                mimetype='application/json'
            )
        except Exception as e:
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
            jwt.decode(token, SECRET_KEY, algorithms='HS256')
        except jwt.DecodeError:
            return APIResponse("유효하지 않은 토큰입니다.", 401, code="JWT001")
        except jwt.ExpiredSignatureError:
            return APIResponse("만료된 토큰입니다.", 401, code="JWT002")
        return func(*args, **kwargs)
    return wrapper
