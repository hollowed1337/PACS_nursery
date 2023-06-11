from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_Group


def create_group(db: Session, group: schem_Group.GroupCreate, cabinet_id: int):

    db_group = BaseModel.Kid_group(name=group.name, cabinet_id=cabinet_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return {
        "status": "Успешно создано",
        "data": db_group
        }


def get_group(db: Session, group_id: int):

    return db.query(BaseModel.Kid_group).filter(BaseModel.Kid_group.id == group_id).first()

def get_group_by_name(db: Session, name: str):

    return db.query(BaseModel.Kid_group).filter(BaseModel.Kid_group.name == name).all()

def get_group_by_cab(db: Session, cab_id: int):

    return db.query(BaseModel.Kid_group).filter(BaseModel.Kid_group.cabinet_id == cab_id).all()

def get_group_by_cab_for_upd(db: Session, cab_id: int):

    return db.query(BaseModel.Kid_group).filter(BaseModel.Kid_group.cabinet_id == cab_id).filter(BaseModel.Kid_group.cabinet_id != cab_id).all()

def get_group_cab(db: Session, cab_id: int):

    return db.query(BaseModel.Cabinet).filter(BaseModel.Cabinet.id == cab_id).all()

def read_groups(db: Session, skip:int=0, limit:int=100):

    return db.query(BaseModel.Kid_group).offset(skip).limit(limit).all()


def update_group(db: Session,  group_id: int, group: schem_Group.GroupUpdate):

    db.query(BaseModel.Kid_group).filter(BaseModel.Kid_group.id == group_id).update(
        {
        BaseModel.Kid_group.name: group.name,
        BaseModel.Kid_group.cabinet_id: group.cabinet_id
        }, synchronize_session="fetch"
    )
    db.commit()
    return {
        "status": f"Запись {group_id} изменена",
        "data" : db.query(BaseModel.Kid_group).filter(BaseModel.Kid_group.id == group_id).first()
        }


def delete_group(db: Session, group_id: int):

    db_group = db.query(BaseModel.Kid_group).filter(BaseModel.Kid_group.id == group_id).first()
    db.delete(db_group)
    db.commit()
    return {
        "status": f"Запись {group_id} удалена",
        "data": db_group
        }