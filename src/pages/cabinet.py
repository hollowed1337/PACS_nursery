from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_Cab,rout_People
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_Cabinet"]
)

templates_cabinet = Jinja2Templates(directory="src/templates/cabinet")


@router.get("/cabinets")
def get_cabs_page(request: Request, cabinets = Depends(rout_Cab.read_cabs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_cabinet.TemplateResponse("cabinets.html", {"request": request, "cabinets": cabinets, "auth": auth, "peoples": peoples})


@router.get("/cabinets/create") #
def create_cab_page(request: Request, auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_cabinet.TemplateResponse("cabinet_create.html", {"request": request, "auth": auth, "peoples": peoples})


@router.get("/cabinet/{cab_id}")
def get_cab_page(request: Request, cab = Depends(rout_Cab.get_cab), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_cabinet.TemplateResponse("cabinet.html", {"request": request, "cab": cab, "auth": auth, "peoples": peoples})


@router.get("/cabinet/edit/{cab_id}") #
def edit_cab_page(request: Request,  cab = Depends(rout_Cab.get_cab), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_cabinet.TemplateResponse("cabinet_edit.html", {"request": request, "cab": cab, "auth": auth, "peoples": peoples})


@router.get("/cabinet/delete/{cab_id}")
def delete_cab_page(request: Request, cab = Depends(rout_Cab.get_cab), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_cabinet.TemplateResponse("cabinet_delete.html", {"request": request, "cab": cab, "auth": auth, "peoples": peoples})



