from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.auth.router import akb_soc
from src.database import SessionLocal
from src.router import rout_Card, rout_People

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_Card"]
)


templates_card = Jinja2Templates(directory="src/templates/card")




@router.get("/cards")
def get_cards_page(request: Request, cards = Depends(rout_Card.read_cards), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_card.TemplateResponse("cards.html", {"request": request, "cards": cards, "peoples": peoples, "auth":auth})


@router.get("/cards/people={people_id}")
def get_cards_by_people_id_page(request: Request, cards = Depends(rout_Card.read_cards_by_people_id), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_card.TemplateResponse("cards.html", {"request": request, "cards": cards, "peoples": peoples, "auth":auth})


@router.get("/cards/create")
def create_card_page(request: Request, peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_card.TemplateResponse("card_create.html", {"request": request, "peoples": peoples, "auth":auth})


@router.get("/card/{card_id}")
def get_card_page(request: Request, card = Depends(rout_Card.get_card), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_card.TemplateResponse("card.html", {"request": request, "card": card, "peoples": peoples, "auth":auth})

@router.get("/card/edit/{card_id}")
def edit_card_page(request: Request, card = Depends(rout_Card.get_card), peoples = Depends(rout_People.read_peoples),auth = Depends(akb_soc)):
    
    return templates_card.TemplateResponse("card_edit.html", {"request": request, "card": card, "peoples": peoples, "auth":auth})

@router.get("/card/delete/{card_id}")
def delete_card_page(request: Request, card = Depends(rout_Card.get_card), peoples = Depends(rout_People.read_peoples),auth = Depends(akb_soc)):
    
    return templates_card.TemplateResponse("card_delete.html", {"request": request, "card": card, "peoples": peoples, "auth":auth})

