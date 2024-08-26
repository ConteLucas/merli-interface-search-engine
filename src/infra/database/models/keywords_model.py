from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class KeywordsModel(Base):
    __tablename__ = 'keywords'

    id = Column(Integer, primary_key=True, autoincrement=True)
    keyword = Column(String, unique=True, nullable=False)
    user_id = Column(String, nullable=False)
    auth_token = Column(String, nullable=False)
    search_count = Column(Integer, default=1)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, keyword: str, user_id: str, auth_token: str, search_count: int = 1):
        self.keyword = keyword
        self.user_id = user_id
        self.auth_token = auth_token
        self.search_count = search_count
