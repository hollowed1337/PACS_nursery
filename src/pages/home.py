from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_People
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_Home"]
)

templates_base = Jinja2Templates(directory="src/templates")
templates_home = Jinja2Templates(directory="src/templates/home")


@router.get("/base")
def get_base_page(request: Request):
    
    return templates_base.TemplateResponse("base.html", {"request": request})


@router.get("/home")
def get_home_page(request: Request, auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_home.TemplateResponse("home.html", {"request": request, "auth": auth, "peoples": peoples})
