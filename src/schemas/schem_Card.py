from pydantic import BaseModel, Field
from datetime import date

class CardBase(BaseModel):

    people_id: int
    code: str = Field(max_length=8)
    status: bool


class CardCreate(CardBase):
    pass


class CardUpdate(BaseModel):

    activate_date: date
    deactivate_date: date
    status: bool

class Card(CardBase):

    activate_date: date
    deactivate_date: date
    id: int

    class Config:
        orm_mode = True