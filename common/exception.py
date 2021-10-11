from enum import Enum


class APIException(Exception):
    def __init__(self, data: Enum, *args, **kwargs):
        self.code = data.value[0]
        self.message = data.value[1]
        self.status = data.value[2] or 400
        self.extra = kwargs
        super().__init__(self.message)
