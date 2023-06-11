from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_People_D, rout_People, rout_Door
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_PD"]
)


templates_pd = Jinja2Templates(directory="src/templates/people_d")




@router.get("/people_ds")
def get_cards_page(request: Request, pds = Depends(rout_People_D.read_people_doors), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pd.TemplateResponse("people_ds.html", {"request": request, "pds": pds, "auth": auth, "peoples": peoples})


@router.get("/people_ds/create") #
def create_people_d_page(request: Request, peoples = Depends(rout_People.read_peoples), doors = Depends(rout_Door.read_doors), auth = Depends(akb_soc)):
    
    return templates_pd.TemplateResponse("people_d_create.html", {"request": request, "peoples": peoples, "doors": doors, "auth": auth})


@router.get("/people_d/{people_door_id}")
def get_people_d_page(request: Request, people_d = Depends(rout_People_D.get_people_door), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pd.TemplateResponse("people_d.html", {"request": request, "pd": people_d, "auth": auth, "peoples": peoples})



@router.get("/people_d/edit/{people_door_id}") #
def edit_people_d_page(request: Request, pd = Depends(rout_People_D.get_people_door), doors = Depends(rout_Door.read_doors), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pd.TemplateResponse("people_d_edit.html", {"request": request, "pd":pd, "peoples": peoples, "doors": doors, "auth": auth})


@router.get("/people_d/delete/{people_door_id}")
def delete_people_d_page(request: Request, people_d = Depends(rout_People_D.get_people_door), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pd.TemplateResponse("people_d_delete.html", {"request": request, "pd": people_d, "auth": auth, "peoples": peoples})