from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str

    class Config:
        orm_mode = True

class UserDB(UserBase):
    login: str
    password: str

class UserCheck(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

class UserShow(UserBase):
    id: int

    class Config:
        orm_mode = True
