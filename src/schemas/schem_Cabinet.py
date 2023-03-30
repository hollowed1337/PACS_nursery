from pydantic import BaseModel

class CabinetBase(BaseModel):

    num_cabinet: str

class CabinetCreate(CabinetBase):
    pass

class CabinetUpdate(BaseModel):

    num_cabinet: str


class Cabinet(CabinetBase):

    id: int

    class Config: 
        orm_mode = True