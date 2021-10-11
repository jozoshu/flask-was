from sqlalchemy import func

from common.exception import APIException
from common.response.client_error import Http4XX
from .models import LastCrawlDate, ProcessCollection


class GetLastCrawl:
    """크롤러가 마지막으로 수집한 날짜 반환"""

    def __init__(self, params: dict):
        self.params = params
        self.handler_type = None

    def validate(self):
        handler_type = self.params.get('type')
        if not isinstance(handler_type, str):
            raise APIException(Http4XX.INVALID_PARAMS, **self.params)

        self.handler_type = handler_type.upper()

    def get_data(self):
        result = LastCrawlDate.query.filter_by(
            handler_type=self.handler_type
        ).all()

        if len(result) == 0:
            raise APIException(Http4XX.NOT_FOUND, type=self.handler_type)

        return [r.to_json() for r in result]

    def run(self):
        self.validate()
        return self.get_data()


class GetCollecionStatus:
    """크롤러가 수집한 데이터 상태 반환"""

    def __init__(self, params: dict):
        self.params = params
        self.handler_type = None

    def validate(self):
        handler_type = self.params.get('type')
        if not isinstance(handler_type, str):
            raise APIException(Http4XX.INVALID_PARAMS, **self.params)

        self.handler_type = handler_type.upper()

    def get_data(self):
        result = (
            ProcessCollection.query.with_entities(
                ProcessCollection.status,
                func.count().label('count')
            )
            .filter_by(handler_type=self.handler_type)
            .group_by(ProcessCollection.status)
            .all()
        )
        return [{'status': r.status, 'count': r.count} for r in result]

    def run(self):
        self.validate()
        return self.get_data()
