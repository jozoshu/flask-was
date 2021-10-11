from enum import Enum


class Http4XX(Enum):
    INVALID_PARAMS = ('E001', '유효하지 않은 파라미터입니다.', 400)
    NOT_FOUND = ('E002', '데이터를 찾을 수 앖습니다.', 400)
    WRONG_PASSWORD = ('E003', '패스워드가 일치하지 않습니다.', 400)
    INVALID_PHONE_NUMBER = ('E004', '이미 존재하는 휴대폰 번호입니다.', 400)
    WRONG_EMAIL = ('E005', '계정이 존재하지 않습니다.', 400)
