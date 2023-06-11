from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_People_G, rout_People, rout_Group
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_PG"]
)


templates_pg = Jinja2Templates(directory="src/templates/people_g")




@router.get("/people_gs")
def get_people_g_page(request: Request, pgs = Depends(rout_People_G.read_people_groups), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pg.TemplateResponse("people_gs.html", {"request": request, "pgs": pgs, "auth": auth, "peoples": peoples})


@router.get("/people_gs/create") #
def create_people_g_page(request: Request, peoples = Depends(rout_People.read_peoples), groups = Depends(rout_Group.read_groups), auth = Depends(akb_soc)):
    
    return templates_pg.TemplateResponse("people_g_create.html", {"request": request, "peoples": peoples, "groups": groups, "auth": auth})


@router.get("/people_g/{people_group_id}")
def get_people_g_page(request: Request, people_g = Depends(rout_People_G.get_people_group), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pg.TemplateResponse("people_g.html", {"request": request, "pg": people_g, "auth": auth, "peoples": peoples})

@router.get("/people_g/edit/{people_group_id}")
def edit_people_g_page(request: Request, pg = Depends(rout_People_G.get_people_group), peoples = Depends(rout_People.read_peoples), groups = Depends(rout_Group.read_groups), auth = Depends(akb_soc)):
    
    return templates_pg.TemplateResponse("people_g_edit.html", {"request": request, "pg": pg, "peoples": peoples, "groups": groups, "auth": auth})


@router.get("/people_g/delete/{people_group_id}")
def delete_people_g_page(request: Request, people_g = Depends(rout_People_G.get_people_group), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pg.TemplateResponse("people_g_delete.html", {"request": request, "pg": people_g, "auth": auth, "peoples": peoples})