from enum import Enum


class Http4XX(Enum):
    BAE_REQUEST = ('E001', '잘못된 요청.', 401)
    INVALID_TOKEN = ('E002', '유효하지 않은 토큰입니다.', 401)
    EXPIRED_TOKEN = ('E003', '만료된 토큰입니다.', 401)
    NOT_FOUND = ('E004', '데이터를 찾을 수 앖습니다.', 404)
    INVALID_PARAMS = ('E005', '유효하지 않은 파라미터입니다.', 400)
    WRONG_PASSWORD = ('E006', '패스워드가 일치하지 않습니다.', 400)
    INVALID_PHONE_NUMBER = ('E007', '이미 존재하는 휴대폰 번호입니다.', 400)
    WRONG_EMAIL = ('E008', '계정이 존재하지 않습니다.', 400)
