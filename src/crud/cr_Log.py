from sqlalchemy.orm import Session
from src.model import BaseModel
from datetime import datetime, timedelta


def get_log(db: Session, log_id: int):

    return db.query(BaseModel.Log).filter(BaseModel.Log.id == log_id).first()


def read_logs(db: Session, skip:int=0, limit:int=20):

    return db.query(BaseModel.Log).offset(skip).limit(limit).all()


def between_time(db: Session, start_dt: datetime, end_dt: datetime, skip:int=0, limit:int=20):
    
    start_dt = start_dt.strftime("%Y-%m-%dT%H:%M")
    end_dt = end_dt.strftime("%Y-%m-%dT%H:%M")
    if start_dt > end_dt:
        return {
            "status": "error",
            "detail": "Стартовое время должно быть меньше"
        }
    else:
        return db.query(BaseModel.Log).filter(BaseModel.Log.date >= start_dt).filter(BaseModel.Log.date <= end_dt).offset(skip).limit(limit).all()
    
    
def read_logs_by_people(db: Session, people_id: int):
    
    people = BaseModel.People.id = people_id #получам запись человека по введенному ID
    card = BaseModel.Card.people_id = people #подставляем ID полученного человека и получаем запись карты
    return db.query(BaseModel.Log).filter(BaseModel.Log.id_card == card).all()


def read_logs_by_door(db: Session, door_id: int, start_dt: datetime, end_dt: datetime, skip:int=0, limit:int=20):
    
    card = BaseModel.Log.card
    people = BaseModel.Card.people
    door_p = BaseModel.Door_People.door
    d_id_p = BaseModel.Door.id
    
    reader = BaseModel.Log.reader
    cab = BaseModel.Reader.cabinet
    door_c = BaseModel.Cabinet.door
    d_id_c = BaseModel.Door.id
    type_door = BaseModel.Door.type_door
    log = db.query(BaseModel.Log).filter(card).filter(people).filter(door_p).filter(d_id_p == door_id).filter(reader).filter(cab).filter(door_c).filter(d_id_c == door_id).filter(type_door =="Шкафчик")
    

    start_dt = start_dt.strftime("%Y-%m-%dT%H:%M")
    end_dt = end_dt.strftime("%Y-%m-%dT%H:%M")
    if start_dt > end_dt:
        return {
            "status": "error",
            "detail": "Стартовое время должно быть меньше"
        }
    else:
        return log.filter(BaseModel.Log.date >= start_dt).filter(BaseModel.Log.date <= end_dt).offset(skip).limit(limit).all()

    
    
