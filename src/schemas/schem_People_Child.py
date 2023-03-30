from pydantic import BaseModel


class PChBase(BaseModel):

    people_id: int
    child_id: int

class PChCreate(PChBase):
    pass


class PChUpdate(BaseModel):

    people_id: int
    child_id: int

class PCh(PChBase):

    id: int

    class Config:
        orm_mode = True