from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func

Base = declarative_base()

class Price(Base):
    __tablename__ = 'prices'

    id = Column('id', Integer(), primary_key=True)
    pair = Column('currency', String(), nullable=False)
    last_bid_price = Column('price', Float(), nullable=False)
    created_at = Column('date_', DateTime(), default=func.now())