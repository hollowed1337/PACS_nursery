from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_People_Child



def create_PCh(db: Session, people_id: int, child_id: int):

    db_PCh = BaseModel.People_Child(people_id=people_id, child_id=child_id)
    db.add(db_PCh)
    db.commit()
    db.refresh(db_PCh)
    return {
        "status": "Успешно создано",
        "data": db_PCh
        }


def get_PCh(db: Session, people_child_id: int):

    return db.query(BaseModel.People_Child).filter(BaseModel.People_Child.id == people_child_id).first()

def get_PCh_people(db: Session, people_id: int):

    return db.query(BaseModel.People).filter(BaseModel.People.id == people_id).all()


def get_PCh_child(db: Session, child_id: int):

    return db.query(BaseModel.Child).filter(BaseModel.Child.id == child_id).all()


def get_PCh_by_child(db: Session, child_id: int):

    return db.query(BaseModel.People_Child).filter(BaseModel.People_Child.child_id == child_id).all()


def get_PCh_by_people(db: Session, people_id: int):

    return db.query(BaseModel.People_Child).filter(BaseModel.People_Child.people_id == people_id).all()


def get_PCh_by_pch(db: Session, people_id: int, child_id: int):

    return db.query(BaseModel.People_Child).filter(BaseModel.People_Child.people_id == people_id).filter(BaseModel.People_Child.child_id == child_id).first()

def read_PChs(db: Session, skip:int=0, limit:int=100):

    return db.query(BaseModel.People_Child).offset(skip).limit(limit).all()


def update_PCh(db: Session, people_child_id: int, pch: schem_People_Child.PChCreate):

    db.query(BaseModel.People_Child).filter(BaseModel.People_Child.id == people_child_id).update(
        {
        BaseModel.People_Child.people_id: pch.people_id, 
        BaseModel.People_Child.child_id: pch.child_id
        }, synchronize_session="fetch"
    )
    db.commit()
    return {
        "status": f"Запись {people_child_id} изменена",
        "data" : db.query(BaseModel.People_Child).filter(BaseModel.People_Child.id == people_child_id).first()
        } 

def delete_PCh(db: Session, people_child_id: int):

    db_PCh = db.query(BaseModel.People_Child).filter(BaseModel.People_Child.id == people_child_id).first()
    db.delete(db_PCh)
    db.commit()
    return {
        "status": f"Запись {people_child_id} удалена",
        "data": db_PCh
        }