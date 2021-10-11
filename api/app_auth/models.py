from re import T
from sqlalchemy import Column, Integer, String, DateTime, Boolean, func

from common.models import BaseModel


class User(BaseModel):
    id = Column(Integer, primary_key=True)
    user_name = Column(String(32), nullable=True)
    phone_number = Column(String(16), unique=True)
    user_email = Column(String(128), unique=True)
    password = Column(String(128))
    is_active = Column(Boolean(), default=True)
    is_admin = Column(Boolean(), default=False)
    created_dtm = Column(DateTime(timezone=True), default=func.now())
    last_login_dtm = Column(DateTime(timezone=True), nullable=True)
    updated_dtm = Column(DateTime(timezone=True), nullable=True)

    __tablename__ = 'tb_user'
