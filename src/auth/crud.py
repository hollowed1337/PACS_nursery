from sqlalchemy.orm import Session
from passlib.context import CryptContext

from src.model import BaseModel


pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_user_by_phone(phone: str, db: Session):
    try:
        user = db.query(BaseModel.People).filter(
            BaseModel.People.phone == phone).one()
        return user
    except Exception:
        return None


def authenticate_user(phone: str, password: str, db: Session):
    user = get_user_by_phone(phone, db)
    if not user:
        return False
    if not verify_password(password, pwd_context.hash(user.password)):
        return False
    return user

