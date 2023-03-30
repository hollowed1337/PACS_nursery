from pydantic import BaseModel

class ReaderBase(BaseModel):
    
    cabinet_id: int
    serial_num: str

class ReaderCreate(ReaderBase):
    pass

class Reader(ReaderBase):

    id: int

    class Config: 
        orm_mode = True