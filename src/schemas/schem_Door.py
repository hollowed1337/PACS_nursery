from pydantic import BaseModel


class DoorBase(BaseModel):

    door_num: str
    cabinet_id: int


class DoorCreate(DoorBase):
    pass


class DoorUpdate(BaseModel):

    door_num: str


class Door(DoorBase):

    id: int

    class Config:
        orm_mode = True