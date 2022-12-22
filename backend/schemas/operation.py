from datetime import date
from typing import List
from pydantic import BaseModel

from schemas.substance import SubstanceShow
from schemas.operationType import Operation_Type
from schemas.user import UserShow

class OperationBase(BaseModel):
    date: date
    amount: int

    class Config:
        orm_mode = True

class OperationCreate(OperationBase):
    substance: str
    type: str
    user: str

class OperationUpdate(OperationBase):
    substance: str
    type: str
    user: str

    class Config:
        orm_mode = True

class Operation(OperationBase):  
    id: int 
    substance:  SubstanceShow
    type: Operation_Type
    user: UserShow 

    class Config:
        orm_mode = True