from enum import Enum


class Http4XX(Enum):
    INVALID_PARAMS = ('E001', '유효하지 않은 파라미터입니다.', 400)
    NOT_FOUND = ('E002', '데이터를 찾을 수 앖습니다.', 400)
