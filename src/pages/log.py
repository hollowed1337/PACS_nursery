from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_Log, rout_Child, rout_People
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_Log"]
)


templates_card = Jinja2Templates(directory="src/templates/log")


@router.get("/logs")
def get_logs_page(request: Request, logs = Depends(rout_Log.read_logs), kids = Depends(rout_Child.read_childs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_card.TemplateResponse("logs.html", {"request": request, "logs": logs, "kids": kids, "auth": auth, "peoples": peoples})

@router.get("/logs_between")
def get_logs_page(request: Request, logs = Depends(rout_Log.between_time), kids = Depends(rout_Child.read_childs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_card.TemplateResponse("logs.html", {"request": request, "logs": logs, "kids": kids, "auth": auth, "peoples": peoples})


@router.get("/log/{log_id}")
def get_log_page(request: Request, log = Depends(rout_Log.get_log), kids = Depends(rout_Child.read_childs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
   return templates_card.TemplateResponse("log.html", {"request": request, "log": log, "kids": kids, "auth": auth, "peoples": peoples})


# @router.get("/logs/role")
# def get_logs_role_page(request: Request, logs = Depends(rout_Log.between_time)):

    # return templates_card.TemplateResponse("logs_role.html", {"request": request, "logs": logs})


@router.get("/logs/child_door={door_id}")
def get_logs_child_page(request: Request, logs = Depends(rout_Log.read_logs_by_childDoor), kids = Depends(rout_Child.read_childs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):

    return templates_card.TemplateResponse("logs_child_cab.html", {"request": request, "logs": logs, "kids": kids, "auth": auth, "peoples": peoples})

@router.get("/logs/diagramm/child_door={door_id}")
def get_logs__dia_child_page(request: Request, logs = Depends(rout_Log.read_logs_by_childDoor), kids = Depends(rout_Child.read_childs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):

    return templates_card.TemplateResponse("logs_dia.html", {"request": request, "logs": logs, "kids": kids, "auth": auth, "peoples": peoples})