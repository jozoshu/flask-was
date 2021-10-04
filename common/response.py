from functools import wraps
import json

from flask import Response

from common.exceptions import APIException


def success(data: object) -> dict:
    res = {
        'code': 'S000',
        'data': data,
    }
    return res


def exception(ae: APIException) -> dict:
    res = {
        'error': ae.code,
        'msg': ae.message,
    }
    return res


def error(e: Exception) -> dict:
    res = {
        'error': type(e).__name__,
        'msg': str(e),
    }
    return res


def send_format(func):
    """Response 기본 형태"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            return Response(
                response=json.dumps(success(response)),
                status=200,
                mimetype='application/json'
            )
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
