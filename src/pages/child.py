from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_Child, rout_Group, rout_Door, rout_People
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_Child"]
)


templates_child = Jinja2Templates(directory="src/templates/child")



@router.get("/kids")
def get_kids_page(request: Request, kids = Depends(rout_Child.read_childs), groups = Depends(rout_Group.read_groups), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_child.TemplateResponse("kids.html", {"request": request, "kids": kids, "groups": groups, "auth": auth, "peoples": peoples})

@router.get("/kids/group={group_id}")
def get_kids_by_group_page(request: Request, kids = Depends(rout_Child.read_childs_by_group), groups = Depends(rout_Group.read_groups), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
     return templates_child.TemplateResponse("kids.html", {"request": request, "kids": kids, "groups": groups, "auth": auth, "peoples": peoples})


@router.get("/kids/create") #
def create_kid_page(request: Request, groups = Depends(rout_Group.read_groups), doors= Depends(rout_Door.read_doors), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_child.TemplateResponse("kid_create.html", {"request": request, "groups": groups, "doors": doors, "auth": auth, "peoples": peoples})


@router.get("/kid/{child_id}")
def get_kid_page(request: Request, kid = Depends(rout_Child.get_child), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_child.TemplateResponse("kid.html", {"request": request, "kid": kid, "auth": auth, "peoples": peoples})


@router.get("/kid/edit/{child_id}") #
def edit_kid_page(request: Request, kid = Depends(rout_Child.get_child), groups = Depends(rout_Group.read_groups), doors= Depends(rout_Door.read_doors), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_child.TemplateResponse("kid_edit.html", {"request": request, "kid":kid, "groups": groups, "doors": doors, "auth": auth, "peoples": peoples})

@router.get("/kid/delete/{child_id}")
def delete_kid_page(request: Request, kid = Depends(rout_Child.get_child), peoples = Depends(rout_People.read_peoples), auth = Depends(akb_soc)):
    
    return templates_child.TemplateResponse("kid_delete.html", {"request": request, "kid": kid, "auth": auth, "peoples": peoples})