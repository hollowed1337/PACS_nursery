from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_Reader


def create_reader(db: Session, reader: schem_Reader.ReaderCreate):

    db_reader = BaseModel.Reader(serial_num=reader.serial_num, cabinet_id=reader.cabinet_id)
    db.add(db_reader)
    db.commit()
    db.refresh(db_reader)
    return db_reader


def get_reader(db: Session, reader_id: int):

    return db.query(BaseModel.Reader).filter(BaseModel.Reader.id == reader_id).first()

def get_reader_cab(db: Session, cab_id: int):

    return db.query(BaseModel.Cabinet).filter(BaseModel.Cabinet.id == cab_id).first()

def get_reader_by_sernum(db: Session, serial_num: int):

    return db.query(BaseModel.Reader).filter(BaseModel.Reader.serial_num == serial_num).first()


def get_reader_by_cab(db: Session, cab_id: int):

    return db.query(BaseModel.Reader).filter(BaseModel.Reader.cabinet_id == cab_id).first()

def read_readers(db: Session, skip:int = 0, limit:int = 100):

    return db.query(BaseModel.Reader).offset(skip).limit(limit).all()
