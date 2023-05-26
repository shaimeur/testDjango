# from django.db import models
# Create your models here.

from sqlalchemy import Column, Integer, String, Date,Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__  = 'transaction'
    id = Column(Integer, primary_key=True)
    transaction_date = Column(Date)
    amount = Column(Float)
    merchant_name = Column(String(100))
