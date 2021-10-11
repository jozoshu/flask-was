from enum import Enum
import json

from flask import Response

from . import formats


class APIResponse(Response):
    def __init__(self, res: Enum, data: object = None, **kwargs):
        code = res.value[0]
        msg = res.value[1]
        super().__init__(
            response=json.dumps(formats.success(data, msg, code)), 
            status=res.value[2] or 200,
            mimetype='application/json'
        )
