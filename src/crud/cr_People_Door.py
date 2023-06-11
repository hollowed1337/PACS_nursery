from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_People_Door


def create_PD(db: Session, people_id: int, door_id: int):

    db_PD = BaseModel.Door_People(people_id=people_id, door_id=door_id)
    db.add(db_PD)
    db.commit()
    db.refresh(db_PD)
    return {
        "status": "Успешно создано",
        "data": db_PD
        }


def get_PD(db: Session, PD_id: int):

    return db.query(BaseModel.Door_People).filter(BaseModel.Door_People.id == PD_id).first()

def get_PD_people(db: Session, people_id: int):

    return db.query(BaseModel.People).filter(BaseModel.People.id == people_id).all()


def get_PD_door(db: Session, door_id: int):

    return db.query(BaseModel.Door).filter(BaseModel.Door.id == door_id).all()


def get_PD_by_door(db: Session, door_id: int):

    return db.query(BaseModel.Door_People).filter(BaseModel.Door_People.door_id == door_id).all()


def get_PD_by_people(db: Session, people_id: int):

    return db.query(BaseModel.Door_People).filter(BaseModel.Door_People.people_id == people_id).all()

def get_PD_by_p_d(db: Session, people_id: int, door_id: int):

    return db.query(BaseModel.Door_People).filter(BaseModel.Door_People.people_id == people_id).filter(BaseModel.Door_People.door_id == door_id).first()

def read_PDs(db: Session, skip:int=0, limit:int=100):

    return db.query(BaseModel.Door_People).offset(skip).limit(limit).all()


def update_PD(db: Session, PD_id: int, pd: schem_People_Door.PDCreate):

    db.query(BaseModel.Door_People).filter(BaseModel.Door_People.id == PD_id).update(
        {
        BaseModel.Door_People.people_id: pd.people_id, 
        BaseModel.Door_People.door_id: pd.door_id
        }, synchronize_session="fetch"
    )
    db.commit()
    return {
        "status": f"Запись {PD_id} изменена",
        "data" : db.query(BaseModel.Door_People).filter(BaseModel.Door_People.id == PD_id).first()
        } 

def delete_PD(db: Session, PD_id: int):

    db_PD = db.query(BaseModel.Door_People).filter(BaseModel.Door_People.id == PD_id).first()
    db.delete(db_PD)
    db.commit()
    return {
        "status": f"Запись {PD_id} удалена",
        "data": db_PD
        }

