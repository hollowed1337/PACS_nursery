from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.database import SessionLocal
from src.router import rout_Reader, rout_Cab, rout_People
from src.auth.router import akb_soc

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/pages",
    tags=["Pages_Reader"]
)


templates_reader = Jinja2Templates(directory="src/templates/reader")



@router.get("/readers")
def get_cards_page(request: Request, readers = Depends(rout_Reader.read_readers), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_reader.TemplateResponse("readers.html", {"request": request, "readers": readers, "auth": auth, "peoples": peoples})


@router.get("/readers/create")
def create_reader_page(request: Request, cabs = Depends(rout_Cab.read_cabs), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_reader.TemplateResponse("reader_create.html", {"request": request, "cabs": cabs, "auth": auth, "peoples": peoples})


@router.get("/reader/{reader_id}")
def get_reader_page(request: Request, reader = Depends(rout_Reader.get_reader), auth = Depends(akb_soc), peoples = Depends(rout_People.read_peoples)):
    
    return templates_reader.TemplateResponse("reader.html", {"request": request, "reader": reader, "auth": auth, "peoples": peoples})


#@router.get("/reader/edit/{reader_id}") #
#def edit_reader_page(request: Request):
    
#    return templates_reader.TemplateResponse("reader_edit.html", {"request": request})


#@router.get("/reader/delete/{reader_id}")
#def delete_reader_page(request: Request, reader = Depends(rout_Reader.delete_reader)):
    
#    return templates_reader.TemplateResponse("reader_delete.html", {"request": request, "reader": reader})