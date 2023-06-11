from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LogBase(BaseModel):

    id_reader: Optional[int]
    id_card: Optional[int]


#class LogCreate(LogBase):
#    pass


# class LogUpdate(BaseModel):

#     activate_date: datetime
#     deactivate_date: datetime
#     status: bool

class Log(LogBase):

    date: datetime
    id: int

    class Config:
        orm_mode = True