from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Instrument(Base):
    __tablename__ = "instruments"
    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True)
    exchange = Column(String)
    instrument_type = Column(String)
    last_traded_price = Column(Float)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    side = Column(String)
    order_type = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, server_default=func.now())

class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    symbol = Column(String)
    side = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    executed_at = Column(DateTime, server_default=func.now())

class Portfolio(Base):
    __tablename__ = "portfolio"
    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True)
    quantity = Column(Integer)
    avg_price = Column(Float)
