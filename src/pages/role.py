from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_Role, rout_People
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_Role"]
)


templates_role = Jinja2Templates(directory="src/templates/role")




@router.get("/roles")
def get_roles_page(request: Request, roles = Depends(rout_Role.read_roles), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_role.TemplateResponse("roles.html", {"request": request, "roles": roles, "auth": auth, "peoples": peoples})


@router.get("/roles/create") #
def create_role_page(request: Request, auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_role.TemplateResponse("role_create.html", {"request": request, "auth": auth, "peoples": peoples})


@router.get("/role/{role_id}")
def get_role_page(request: Request, role = Depends(rout_Role.get_role), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_role.TemplateResponse("role.html", {"request": request, "role": role, "auth": auth, "peoples": peoples})


@router.get("/role/edit/{role_id}")
def edit_role_page(request: Request, role = Depends(rout_Role.get_role), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_role.TemplateResponse("role_edit.html", {"request": request, "role": role, "auth": auth, "peoples": peoples})


@router.get("/role/delete/{role_id}")
def delete_role_page(request: Request, role = Depends(rout_Role.get_role), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_role.TemplateResponse("role_delete.html", {"request": request, "role": role, "auth": auth, "peoples": peoples})