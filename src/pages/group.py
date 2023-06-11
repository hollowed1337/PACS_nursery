from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_Group, rout_Cab, rout_Door, rout_People
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_Group"]
)


templates_group = Jinja2Templates(directory="src/templates/group")



@router.get("/groups")
def get_groups_page(request: Request, groups = Depends(rout_Group.read_groups), cabs = Depends(rout_Cab.read_cabs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_group.TemplateResponse("groups.html", {"request": request, "groups": groups, "cabs" : cabs, "auth": auth, "peoples": peoples})


@router.get("/groups/cab={cab_id}")

def get_groups_page(request: Request, groups = Depends(rout_Group.read_groups_by_cab), cabs = Depends(rout_Cab.read_cabs), doors = Depends(rout_Door.read_doors), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_group.TemplateResponse("groups.html", {"request": request, "groups": groups, "cabs" : cabs, "doors": doors, "auth": auth, "peoples": peoples})


@router.get("/groups/create") #
def create_group_page(request: Request, cabinets = Depends(rout_Cab.read_cabs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_group.TemplateResponse("group_create.html", {"request": request, "cabs": cabinets, "auth": auth, "peoples": peoples})


@router.get("/group/{group_id}")
def get_group_page(request: Request, group = Depends(rout_Group.get_group), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_group.TemplateResponse("group.html", {"request": request, "group": group, "auth": auth, "peoples": peoples})


@router.get("/group/edit/{group_id}") #
def edit_group_page(request: Request, group = Depends(rout_Group.get_group), cabinets = Depends(rout_Cab.read_cabs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_group.TemplateResponse("group_edit.html", {"request": request,"group": group, "cabs":cabinets, "auth": auth, "peoples": peoples})


@router.get("/group/delete/{group_id}")
def delete_group_page(request: Request, group = Depends(rout_Group.get_group), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_group.TemplateResponse("group_delete.html", {"request": request, "group": group, "auth": auth, "peoples": peoples})