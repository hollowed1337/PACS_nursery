from fastapi import Depends, HTTPException, APIRouter, Path
from sqlalchemy.orm import Session
from src.crud import cr_Reader
from src.schemas import schem_Reader
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@rout.post("/reader", response_model=schem_Reader.Reader)
def create_reader(reader: schem_Reader.ReaderCreate, db: Session = Depends(get_db)):

    db_reader_by_sernum = cr_Reader.get_reader_by_sernum(db, serial_num=reader.serial_num)
    if db_reader_by_sernum:
        raise HTTPException(status_code=400, detail="Серийный номер занят")
    
    db_reader_by_cab = cr_Reader.get_reader_by_cab(db, cab_id=reader.cabinet_id)    
    if db_reader_by_cab:
        raise HTTPException(status_code=400, detail="Считыватель в данном кабинете уже стоит")

    db_reader_cab = cr_Reader.get_reader_cab(db, cab_id=reader.cabinet_id)
    if not db_reader_cab:
        raise HTTPException(status_code=404, detail="Запись не найдена")

    return cr_Reader.create_reader(db=db, reader=reader)

@rout.get("/reader/{reader_id}", response_model=schem_Reader.Reader)
def get_reader(reader_id: int, db: Session = Depends(get_db)):

    db_reader = cr_Reader.get_reader(db, reader_id=reader_id)
    if not db_reader:
        raise HTTPException(status_code=404, detail="Записи не существует")
    return db_reader


@rout.get("/readers", response_model=list[schem_Reader.Reader])
def read_readers(skip: int=0, limit: int=100, db: Session = Depends(get_db)):

    return cr_Reader.read_readers(db, skip=skip, limit=limit)