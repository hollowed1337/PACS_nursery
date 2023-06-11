from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_Cabinet
from src.schemas import schem_Cabinet
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Кабинет

@rout.post("/cab")
async def create_cab(cab: schem_Cabinet.CabinetCreate, db: Session = Depends(get_db)):

    db_cab = cr_Cabinet.get_cab_by_num(db, num_cabinet=cab.num_cabinet)
    if db_cab:
        raise HTTPException(status_code=404, detail="Запись уже существует")
    
    return cr_Cabinet.create_cab(db=db, cab=cab)

@rout.get("/cab/{cab_id}", response_model=schem_Cabinet.Cabinet)
async def get_cab(cab_id: int, db: Session = Depends(get_db)):

    db_cab = cr_Cabinet.get_cab(db, cab_id=cab_id)
    if not db_cab:
        raise HTTPException(status_code=404, detail="Записи не существует")
    return db_cab


@rout.get("/cabs", response_model= list[schem_Cabinet.Cabinet])
async def read_cabs(skip:int=0, limit:int=100, db: Session = Depends(get_db)):

    return cr_Cabinet.read_cabs(db, skip=skip, limit=limit)


@rout.put("/cab/{cab_id}")
async def edit_cab(cab: schem_Cabinet.CabinetUpdate, cab_id: int, db: Session = Depends(get_db)):

    db_cab = cr_Cabinet.get_cab(db, cab_id=cab_id)
    if not db_cab:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    
    db_cab = cr_Cabinet.get_cab_by_num(db, num_cabinet=cab.num_cabinet)
    if db_cab:
        raise HTTPException(status_code=404, detail="Запись уже существует")
    
    return cr_Cabinet.update_cab(db, cab_id=cab_id, cab=cab)

@rout.delete("/cab/{cab_id}")
async def delete_cab(cab_id: int, db: Session = Depends(get_db)):

    db_cab = cr_Cabinet.get_cab(db, cab_id=cab_id)
    if not db_cab:
        raise HTTPException(status_code=404, detail="Невозможно удалить несуществующую запись")
    return cr_Cabinet.delete_cab(db, cab_id=cab_id)
