from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_Door, rout_Cab, rout_People
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_Door"]
)


templates_door = Jinja2Templates(directory="src/templates/door")


@router.get("/doors")
def get_doors_page(request: Request, doors = Depends(rout_Door.read_doors), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_door.TemplateResponse("doors.html", {"request": request, "doors": doors, "auth": auth, "peoples": peoples})


@router.get("/doors/create") #
def create_door_page(request: Request, cabs = Depends(rout_Cab.read_cabs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_door.TemplateResponse("door_create.html", {"request": request, "cabs": cabs, "auth": auth, "peoples": peoples})


@router.get("/door/{door_id}")
def get_door_page(request: Request, door = Depends(rout_Door.get_door), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_door.TemplateResponse("door.html", {"request": request, "door": door, "auth": auth, "peoples": peoples})

@router.get("/door/edit/{door_id}") #
def edit_door_page(request: Request, door = Depends(rout_Door.get_door), cabs = Depends(rout_Cab.read_cabs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_door.TemplateResponse("door_edit.html", {"request": request, "door": door, "cabs": cabs, "auth": auth, "peoples": peoples})

@router.get("/door/delete/{door_id}")
def delete_door_page(request: Request, door = Depends(rout_Door.get_door), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_door.TemplateResponse("door_delete.html", {"request": request, "door": door, "auth": auth, "peoples": peoples})