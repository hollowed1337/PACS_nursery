from pydantic import BaseModel, Field
from typing import Optional

class PeopleBase(BaseModel):

    name: str= Field(min_length=5)
    phone: str = Field(regex="[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", max_length=10, description="Номер телефона не может привышать более 10 символов и должен соответствовать x(xxx)xxx-xx-xx")
    password: str
    role_id: int


class PeopleCreate(PeopleBase):

    pass

class PeopleUpdate(BaseModel):

    name: str = Field(min_length=5)
    phone: str = Field(regex="[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", max_length=10, description="Номер телефона не может привышать более 10 символов и должен соответствовать x(xxx)xxx-xx-xx")
    role_id: int

class People(PeopleBase):

    id: int

    class Config:
        orm_mode = True