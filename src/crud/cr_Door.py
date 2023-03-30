from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_Door


def create_door(db: Session, door: schem_Door.DoorCreate):

    db_door = BaseModel.Door(door_num=door.door_num, cabinet_id=door.cabinet_id)
    db.add(db_door)
    db.commit()
    db.refresh(db_door)
    return db_door


def get_door(db: Session, door_id: int):

    return db.query(BaseModel.Door).filter(BaseModel.Door.id == door_id).first()

def get_door_by_num(db: Session, door_num: int):

    return db.query(BaseModel.Door).filter(BaseModel.Door.door_num == door_num).all()

def get_door_by_cab(db: Session, cabinet_id: int):

    return db.query(BaseModel.Door).filter(BaseModel.Door.cabinet_id==cabinet_id).all()

def read_doors(db: Session, skip:int=0, limit:int=100):

    return db.query(BaseModel.Door).offset(skip).limit(limit).all()



def update_door(db: Session, door_id: int, door: schem_Door.DoorUpdate):

    db.query(BaseModel.Door).filter(BaseModel.Door.id == door_id).update(
        {
        BaseModel.Door.door_num: door.door_num,
        }, synchronize_session="fetch"
    )
    db.commit()
    return db.query(BaseModel.Door).filter(BaseModel.Door.id == door_id).first()

def delete_door(db: Session, door_id: int):

    db_door = db.query(BaseModel.Door).filter(BaseModel.Door.id == door_id).first()
    db.delete(db_door)
    db.commit()
    return db_door