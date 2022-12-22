from typing import List
from pydantic import BaseModel


class SubstanceBase(BaseModel):
    element_number: int 
    name: str 
    cas: str 
    formula: str 
    units: str
    type: str

    class Config:
        orm_mode = True

class SubstanceCreate(SubstanceBase):
    pass

class SubstanceShow(SubstanceBase):
    id: int

    class Config:
        orm_mode = True
