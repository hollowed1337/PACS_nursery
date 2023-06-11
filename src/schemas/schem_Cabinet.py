from pydantic import BaseModel, Field

class CabinetBase(BaseModel):

    num_cabinet: str = Field(max_length=3)

class CabinetCreate(CabinetBase):
    pass

class CabinetUpdate(BaseModel):

    num_cabinet: str = Field(max_length=3)


class Cabinet(CabinetBase):

    id: int

    class Config: 
        orm_mode = True