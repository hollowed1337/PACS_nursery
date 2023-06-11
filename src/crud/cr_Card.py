from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from src.model import BaseModel
from src.schemas import schem_Card

def create_card(db: Session, card: schem_Card.CardCreate, people_id: int):
    
    activ_date = datetime.now()
    d = timedelta(365)
    deactiv_date = activ_date + d
    db_card = BaseModel.Card(code=card.code, activate_date=activ_date, deactivate_date=deactiv_date, status=card.status, people_id=people_id)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return {
        "status": "Успешно создано",
        "data": db_card
        }


def get_card(db: Session, card_id: int):

    return db.query(BaseModel.Card).filter(BaseModel.Card.id == card_id).first()


def get_card_people(db: Session, people_id):

    return db.query(BaseModel.People).filter(BaseModel.People.id == people_id).first()


def get_card_by_people(db: Session, people_id: int):

    return db.query(BaseModel.Card).filter(BaseModel.Card.people_id == people_id).all()


def get_card_by_code(db: Session, code: int):

    return db.query(BaseModel.Card).filter(BaseModel.Card.code == code).first()


def read_cards(db:Session, skip:int = 0, limit:int = 100):

    return db.query(BaseModel.Card).offset(skip).limit(limit).all()


def delete_card(db:Session, card_id:int):
    
    db_card = db.query(BaseModel.Card).filter(BaseModel.Card.id == card_id).first()
    db.delete(db_card)
    db.commit()
    return {
        "status": f"Запись {card_id} удалена",
        "data": db_card
        }


def update_card(db: Session, card_id: int, card: schem_Card.CardUpdate):
    
    db.query(BaseModel.Card).filter(BaseModel.Card.id == card_id).update(
        {
        BaseModel.Card.activate_date: card.activate_date,
        BaseModel.Card.deactivate_date: card.deactivate_date,
        BaseModel.Card.status: card.status
        }, synchronize_session="fetch"
    )
    db.commit()
    return {
        "status": f"Запись {card_id} изменена",
        "data" : db.query(BaseModel.Card).filter(BaseModel.Card.id == card_id).first()
        }


def date(db: Session, card: schem_Card.CardUpdate):

    return db.query(BaseModel.Card).filter(card.activate_date < card.deactivate_date).all()