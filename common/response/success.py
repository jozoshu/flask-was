from enum import Enum


class Http2XX(Enum):
    SUCCESS = ('S001', '성공', 200)
    CREATED = ('S002', '생성 완료', 201)
