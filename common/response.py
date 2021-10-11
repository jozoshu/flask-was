import json

from flask import Response

from common.exceptions import APIException


def success(data: object, code='S000') -> dict:
    res = {
        'code': code,
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


class APIResponse(Response):
    def __init__(self, response: Response, status=200, **kwargs):
        super().__init__(
            response=json.dumps(success(response, **kwargs)), 
            status=status, 
            mimetype='application/json'
        )
