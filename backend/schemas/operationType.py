from typing import List
from pydantic import BaseModel


class Operation_TypeBase(BaseModel):
    type: str

    class Config:
        orm_mode = True    

class Operation_TypeCreate(Operation_TypeBase):
    pass

class Operation_Type(Operation_TypeBase):
    #id: int
    #operations: List[Operation] = []  

    class Config:
        orm_mode = True
