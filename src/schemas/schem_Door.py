from pydantic import BaseModel, Field


class DoorBase(BaseModel):

    door_num: str = Field(max_length=3)
    type_door: str
    cabinet_id: int


class DoorCreate(DoorBase):
    pass


class DoorUpdate(BaseModel):

    door_num: str = Field(max_length=3)
    type_door: str


class Door(DoorBase):

    id: int

    class Config:
        orm_mode = True