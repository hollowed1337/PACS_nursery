from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_Cabinet

def create_cab(db: Session, cab: schem_Cabinet.CabinetCreate):

    db_cab = BaseModel.Cabinet(num_cabinet=cab.num_cabinet)
    db.add(db_cab)
    db.commit()
    db.refresh(db_cab)
    return db_cab


def get_cab(db: Session, cab_id: int):

    return db.query(BaseModel.Cabinet).filter(BaseModel.Cabinet.id == cab_id).first()


def get_cab_by_num(db: Session, num_cabinet: str):

    return db.query(BaseModel.Cabinet).filter(BaseModel.Cabinet.num_cabinet == num_cabinet).all()


def read_cabs(db: Session, skip:int=0, limit:int=100):

    return db.query(BaseModel.Cabinet).offset(skip).limit(limit).all()


def update_cab(db: Session, cab_id: int, cab: schem_Cabinet.CabinetUpdate):

    db.query(BaseModel.Cabinet).filter(BaseModel.Cabinet.id == cab_id).update(
        {
        BaseModel.Cabinet.num_cabinet: cab.num_cabinet
        }, synchronize_session="fetch"
    )
    db.commit()
    return db.query(BaseModel.Cabinet).filter(BaseModel.Cabinet.id == cab_id).first()

def delete_cab(db: Session, cab_id: int):

    db_cab = db.query(BaseModel.Cabinet).filter(BaseModel.Cabinet.id == cab_id).first()
    db.delete(db_cab)
    db.commit()
    return db_cab
    