from pydantic import BaseModel


class PDBase(BaseModel):

    people_id: int
    door_id: int

class PDCreate(PDBase):
    pass


class PDUpdate(BaseModel):

    people_id: int
    door_id: int

class PD(PDBase):

    id: int

    class Config:
        orm_mode = True