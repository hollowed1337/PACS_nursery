from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_Card
from src.schemas import schem_Card
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Карта

@rout.post("/card")
async def create_card(card: schem_Card.CardCreate, db: Session = Depends(get_db)):

    db_card = cr_Card.get_card_by_code(db, code=card.code)
    if db_card:
        raise HTTPException(status_code=404, detail="Запись с таким кодом карты уже существует")
    
    people = cr_Card.get_card_people(db, people_id=card.people_id)
    if not people:
        raise HTTPException(status_code=404, detail="Человека с таким ID не существует") 

    return cr_Card.create_card(db=db, card=card, people_id = card.people_id)

@rout.delete("/card/{card_id}")
def delete_card(card_id: int, db: Session = Depends(get_db)):

    cards = cr_Card.get_card(db, card_id=card_id)
    if not cards:
        raise HTTPException(status_code=404, detail="Невозможно удалить несуществующую запись")
    return cr_Card.delete_card(db, card_id=card_id)

@rout.put("/card/{card_id}")
def edit_card(card: schem_Card.CardUpdate, card_id: int, db: Session = Depends(get_db)):

    cards = cr_Card.get_card(db, card_id=card_id)
    if not cards:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    
    date = cr_Card.date(db, card=card)
    if not date:
        raise HTTPException(status_code=400, detail="Указана неправильная дата")  
    
    return cr_Card.update_card(db, card_id=card_id, card=card)

@rout.get("/card/{card_id}", response_model=schem_Card.Card)
async def get_card(card_id:int, db: Session = Depends(get_db)):

    db_card = cr_Card.get_card(db, card_id=card_id)
    if not db_card:
        raise HTTPException(status_code=404, detail="Записи не существует")
    return db_card

@rout.get("/cards?people={people_id}", response_model=list[schem_Card.Card])
def read_cards_by_people_id(people_id: int, db: Session = Depends(get_db)):

    cards = cr_Card.get_card_by_people(db, people_id=people_id)
    if not cards:
        raise HTTPException(status_code=404, detail="Человека с таким ID не существует или у него отсутствует карта")
    return cards

@rout.get("/cards", response_model=list[schem_Card.Card])
async def read_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    cards = cr_Card.read_cards(db, skip=skip, limit=limit)
    return cards