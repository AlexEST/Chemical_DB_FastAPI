from operator import index
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)

    operations = relationship("Operation", back_populates="user")

class Operation_Type(Base):
    __tablename__ = "operation_type"
    id = Column(Integer,primary_key=True,index=True)
    type = Column(String,unique=True,nullable=False)
    
    operations = relationship("Operation", back_populates="type")
    

class Substance (Base):
    __tablename__ = "substance"
    id = Column(Integer,primary_key = True, index=True)
    element_number = Column(String, nullable=False)
    name = Column(String, nullable=False)
    cas = Column(String, nullable=False)
    formula = Column(String, nullable = False)
    units = Column(String,nullable=False)
    type = Column(String, nullable=False)

    operations = relationship("Operation", back_populates="substance")

class Operation(Base):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True, index=True)
    fk_substance_id = Column(Integer, ForeignKey("substance.id"))
    fk_operation_type_id = Column(Integer, ForeignKey("operation_type.id"))
    fk_user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date, index=True)
    amount = Column(Integer, index=True)

    substance = relationship("Substance", lazy='joined', back_populates="operations")
    user = relationship("User", lazy='joined', back_populates="operations")
    type = relationship("Operation_Type", lazy='joined', back_populates="operations")
    
    
class Stock_Amount (Base):
    __table__ = Table(
    'stock_amount', 
    Base.metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('amount', String),
    Column('units', String),
    )