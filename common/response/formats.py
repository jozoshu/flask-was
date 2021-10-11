from common.exception import APIException


def success(data: object, msg, code) -> dict:
    return {
        'code': code,
        'msg': msg,
        'data': data,
    }


def exception(ae: APIException) -> dict:
    return {
        'code': ae.code,
        'msg': ae.message,
        'data': ae.extra,
    }


def error(e: Exception) -> dict:
    return {
        'error': type(e).__name__,
        'msg': str(e),
    }
