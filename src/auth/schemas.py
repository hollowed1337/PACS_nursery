from pydantic import BaseModel


class User(BaseModel):
    phone: str
    password: str
