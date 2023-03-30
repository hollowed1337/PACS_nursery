from pydantic import BaseModel


class PGBase(BaseModel):

    people_id: int
    group_id: int

class PGCreate(PGBase):
    pass


class PGUpdate(BaseModel):

    people_id: int
    group_id: int

class PG(PGBase):

    id: int

    class Config:
        orm_mode = True