from pydantic import BaseModel
from typing import Optional

class PeopleBase(BaseModel):

    name: str
    phone: str
    role_id: int


class PeopleCreate(PeopleBase):

    pass

class PeopleUpdate(BaseModel):

    name: str
    phone: str
    role_id: int

class People(PeopleBase):

    id: int

    class Config:
        orm_mode = True