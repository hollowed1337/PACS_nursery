from pydantic import BaseModel
from src.schemas import schem_Child

class GroupBase(BaseModel):

    name: str
    cabinet_id: int

class GroupCreate(GroupBase):
    pass

class GroupUpdate(BaseModel):

    name: str
    cabinet_id: int


class Group(GroupBase):

    id: int

    class Config:
        orm_mode = True