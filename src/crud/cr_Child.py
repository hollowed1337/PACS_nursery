from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_Child


def create_child(db: Session, child: schem_Child.ChildCreate):

    db_child = BaseModel.Child(name=child.name, birth_date=child.birth_date, group_id=child.group_id, door_id=child.door_id)
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return {
        "status": "Успешно создано",
        "data" :db_child
        }


def get_child(db: Session, child_id: int):

    return db.query(BaseModel.Child).filter(BaseModel.Child.id == child_id).first()

def get_childs_by_group(db: Session, group_id: int):

    return db.query(BaseModel.Child).filter(BaseModel.Child.group_id == group_id).all()

def get_childs_group(db: Session, group_id: int):

    return db.query(BaseModel.Kid_group).filter(BaseModel.Child.group_id == group_id).all()

def get_child_by_door(db: Session, door_id: int):
    
    return db.query(BaseModel.Child).filter(BaseModel.Child.door_id == door_id).filter(BaseModel.Child.door_id > 0).first()

def get_child_group(db: Session, group_id: int):

    return db.query(BaseModel.Kid_group).filter(BaseModel.Kid_group.id == group_id).first()

def read_childs(db: Session, skip: int=0, limit: int=100):

    return db.query(BaseModel.Child).offset(skip).limit(limit).all()

def update_child(db: Session, child_id: int, child: schem_Child.ChildUpdate):

    db.query(BaseModel.Child).filter(BaseModel.Child.id == child_id).update(
        {
        BaseModel.Child.name: child.name,
        BaseModel.Child.birth_date: child.birth_date,
        BaseModel.Child.group_id: child.group_id,
        BaseModel.Child.door_id: child.door_id
        }, synchronize_session="fetch"
    )
    db.commit()
    return {
        "status" : f"Запись {child_id} изменена",
        "data" :db.query(BaseModel.Child).filter(BaseModel.Child.id == child_id).first()
        }

def delete_child(db: Session, child_id: int):

    db_child = db.query(BaseModel.Child).filter(BaseModel.Child.id == child_id).first()
    db.delete(db_child)
    db.commit()
    return {
        "status": f"Запись {child_id} удалена",
        "data": db_child
        }