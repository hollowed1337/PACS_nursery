from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.auth.router import akb_soc
from src.database import SessionLocal
from src.router import rout_People, rout_Role
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_People"]
)


templates_people = Jinja2Templates(directory="src/templates/people")


@router.get("/peoples/create") # 
def create_people_page(request: Request, roles = Depends(rout_Role.read_roles), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
     
    return templates_people.TemplateResponse("people_create.html", {"request": request, "roles": roles, "auth": auth, "peoples": peoples})

@router.get("/peoples")
def get_peoples_page(request: Request, peoples = Depends(rout_People.read_peoples), roles = Depends(rout_Role.read_roles), auth = Depends(akb_soc)):
    
    return templates_people.TemplateResponse("peoples.html", {"request": request, "peoples": peoples,  "roles": roles, "auth": auth})


@router.get("/peoples/role={role_id}")
def get_peoples_by_role_page(request: Request, peoples = Depends(rout_People.read_peoples_by_role), roles = Depends(rout_Role.read_roles), auth = Depends(akb_soc)):
    
    return templates_people.TemplateResponse("peoples.html", {"request": request, "peoples": peoples, "roles": roles, "auth": auth})

@router.get("/people/{people_id}")
def get_people_page(request: Request, people = Depends(rout_People.get_people), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_people.TemplateResponse("people.html", {"request": request, "people": people, "auth": auth, "peoples": peoples})



@router.get("/people/edit/{people_id}") 
def edit_people_page(request: Request, people = Depends(rout_People.get_people), roles = Depends(rout_Role.read_roles), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_people.TemplateResponse("people_edit.html", {"request": request, "people": people, "roles": roles, "auth": auth, "peoples": peoples})


@router.get("/people/delete/{people_id}")
def delete_people_page(request: Request, people = Depends(rout_People.get_people), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_people.TemplateResponse("people_delete.html", {"request": request, "people": people["status"], "auth": auth, "peoples": peoples})
