from pydantic import BaseModel
from datetime import date

class ChildBase(BaseModel):

    name: str
    birth_date: date
    group_id: int

class ChildCreate(ChildBase):
    pass

class ChildUpdate(BaseModel):

    name: str
    birth_date: date
    group_id: int


class Child(ChildBase):

    id: int

    class Config: 
        orm_mode = True
