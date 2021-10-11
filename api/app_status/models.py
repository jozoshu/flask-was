from sqlalchemy import Column, Integer, String, Date, DateTime

from common.models import BaseModel


class LastCrawlDate(BaseModel):
    id = Column(Integer, primary_key=True)
    handler_type = Column(String(10))
    last_crawl_date = Column(Date())
    created_dtm = Column(DateTime())

    __tablename__ = 'tb_op_last_crawl_date'

    OUTPUTS = ['handler_type', 'last_crawl_date', 'created_dtm']


class ProcessCollection(BaseModel):
    id = Column(Integer, primary_key=True)
    handler_type = Column(String(10))
    position_id = Column(Integer())
    position = Column(String(250))
    company = Column(String(50))
    status = Column(Integer())
    created_dtm = Column(DateTime())
    updated_dtm = Column(DateTime())

    __tablename__ = 'tb_op_process_collecting'


class ProcessPublish(BaseModel):
    id = Column(Integer, primary_key=True)
    handler_type = Column(String(10))
    idx = Column(Integer())
    status = Column(Integer())

    __tablename__ = 'tb_op_process_publish'
