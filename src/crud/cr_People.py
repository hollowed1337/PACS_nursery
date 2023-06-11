from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_People



def create_people(db: Session, people: schem_People.PeopleCreate, role_id: int):

    db_people =BaseModel.People(name=people.name, phone=people.phone, role_id = role_id, password=people.password)
    db.add(db_people)
    db.commit()
    db.refresh(db_people)
    return {
        "status": f"Запись создана",
        "data": db_people
        }


def get_people(db: Session, people_id: int):

    return db.query(BaseModel.People).filter(BaseModel.People.id == people_id).first()


def get_peoples_role(db: Session, role_id: int):

    return db.query(BaseModel.Role).filter(BaseModel.Role.id == role_id).all()


def get_peoples_by_role(db: Session, role_id: int):

  return db.query(BaseModel.People).filter(BaseModel.People.role_id == role_id).all()



def get_people_by_phone(db: Session, phone: str):
    
    return db.query(BaseModel.People).filter(BaseModel.People.phone == phone).first()


def get_people_by_phone_for_udp(db: Session, phone: str, people_id: int):
    
    return db.query(BaseModel.People).filter(BaseModel.People.phone == phone).filter(BaseModel.People.id != people_id).first()


def read_peoples(db: Session, skip: int=0, limit: int=100):

    return db.query(BaseModel.People).offset(skip).limit(limit).all()


def delete_people(db: Session, people_id: int):

    people = db.query(BaseModel.People).filter(BaseModel.People.id == people_id).first()
    db.delete(people)
    db.commit()
    return {
        "status": f"Запись {people_id} удалена",
        "data": people,
        }


def update_people(db: Session, people_id: int, people: schem_People.PeopleUpdate):
    
    db.query(BaseModel.People).filter(BaseModel.People.id == people_id).update(
        {
        BaseModel.People.name: people.name,
        BaseModel.People.phone: people.phone,
        BaseModel.People.role_id: people.role_id
        }
    )
    db.commit()
    return {
        "status": f"Запись {people_id} изменена",
        "data" : db.query(BaseModel.People).filter(BaseModel.People.id == people_id).first()
        }

