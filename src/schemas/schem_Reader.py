from pydantic import BaseModel, Field

class ReaderBase(BaseModel):
    
    cabinet_id: int
    serial_num: str = Field(max_length=10)

class ReaderCreate(ReaderBase):
    pass

class Reader(ReaderBase):

    id: int

    class Config: 
        orm_mode = True