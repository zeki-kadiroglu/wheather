from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import date, timedelta

Base = declarative_base()


class Temperature(Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)
    date = Column(String, nullable=False)
    temp_c = Column(Float, nullable=False)
    temp_f = Column(Float, nullable=False)


