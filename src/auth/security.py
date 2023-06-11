from fastapi import Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from src.database import SessionLocal

from src.auth.crud import authenticate_user

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

security = HTTPBasic()


def get_current_user(
        credentials: HTTPBasicCredentials = Depends(security),
        db: Session = Depends(get_db)):
    phone = credentials.username
    password = credentials.password

    user = authenticate_user(phone, password, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return phone
