from pydantic import BaseModel
from datetime import datetime

class CardBase(BaseModel):

    people_id: int
    code: str
    status: bool


class CardCreate(CardBase):
    pass


class CardUpdate(BaseModel):

    activate_date: datetime
    deactivate_date: datetime
    status: bool

class Card(CardBase):

    activate_date: datetime
    deactivate_date: datetime
    id: int

    class Config:
        orm_mode = True