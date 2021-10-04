from common.utils import encode
from core.app import db


class BaseModel(db.Model):
    __abstract__ = True

    OUTPUTS: list = []

    def to_json(self) -> dict:
        columns = self.OUTPUTS or [m.key for m in self.__table__.columns]
        return {
            key: encode(getattr(self, key))
            for key in columns
        }
