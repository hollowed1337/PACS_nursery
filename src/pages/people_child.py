from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_People_Ch, rout_People, rout_Child
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_PCh"]
)


templates_pch = Jinja2Templates(directory="src/templates/people_ch")



@router.get("/people_chs")
def get_people_chs_page(request: Request, pchs = Depends(rout_People_Ch.read_people_childs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pch.TemplateResponse("people_chs.html", {"request": request, "pchs": pchs, "auth": auth, "peoples": peoples})


@router.get("/people_chs/create")
def create_people_ch_page(request: Request, peoples = Depends(rout_People.read_peoples), kids = Depends(rout_Child.read_childs), auth = Depends(akb_soc)):
    
    return templates_pch.TemplateResponse("people_ch_create.html", {"request": request, "peoples": peoples, "kids": kids, "auth": auth})


@router.get("/people_ch/{people_child_id}")
def get_people_ch_page(request: Request, people_ch = Depends(rout_People_Ch.get_people_child), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pch.TemplateResponse("people_ch.html", {"request": request, "pch": people_ch, "auth": auth, "peoples": peoples})


@router.get("/people_ch/edit/{people_child_id}")
def edit_people_ch_page(request: Request, pch = Depends(rout_People_Ch.get_people_child), peoples = Depends(rout_People.read_peoples), kids = Depends(rout_Child.read_childs), auth = Depends(akb_soc)):
    
    return templates_pch.TemplateResponse("people_ch_edit.html", {"request": request,"pch": pch, "peoples": peoples, "kids": kids, "auth": auth})


@router.get("/people_ch/delete/{people_child_id}")
def delete_people_ch_page(request: Request, pch = Depends(rout_People_Ch.get_people_child), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_pch.TemplateResponse("people_ch_delete.html", {"request": request, "pch": pch, "auth": auth, "peoples": peoples})