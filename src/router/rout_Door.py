from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_Door
from src.schemas import schem_Door
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Дверца

@rout.post("/door", response_model=schem_Door.Door)
async def create_door(door: schem_Door.DoorCreate, db: Session = Depends(get_db)):

    db_door_num = cr_Door.get_door_by_num(db, door_num=door.door_num)
    if db_door_num:
        raise HTTPException(status_code=400, detail="Запись уже существует")
    
    db_door_by_cab = cr_Door.get_door_by_cab(db, cabinet_id=door.cabinet_id)
    if not db_door_by_cab:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return cr_Door.create_door(db=db, door=door)


@rout.get("/door/{door_id}", response_model=schem_Door.Door)
async def get_door(door_id: int, db: Session = Depends(get_db)):

    db_door = cr_Door.get_door(db, door_id=door_id)
    if not db_door:
        raise HTTPException(status_code=404, detail="Записи не существует")
    return db_door

@rout.get("/doors", response_model=list[schem_Door.Door])
async def read_doors(skip: int=0, limit:int=100, db: Session = Depends(get_db)):

    return cr_Door.read_doors(db, skip=skip, limit=limit)


@rout.put("/door/{door_id}", response_model=schem_Door.Door)
async def edit_door(door: schem_Door.DoorUpdate, door_id: int, db: Session = Depends(get_db)):

    db_door = cr_Door.get_door(db, door_id=door_id)
    if not db_door:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    
    db_role_num = cr_Door.get_door_by_num(db, door_num=door.door_num)
    if db_role_num:
        raise HTTPException(status_code=400, detail="Запись уже существует")
    
    return cr_Door.update_door(db, door=door, door_id=door_id)

@rout.delete("/door/{door_id}", response_model=schem_Door.Door)
async def delete_door(door_id: int, db: Session = Depends(get_db)):

    db_door = cr_Door.get_door(db, door_id=door_id)
    if not db_door:
        raise HTTPException(status_code=404, detail="Невозможно удалить несуществующую запись")
    return cr_Door.delete_door(db, door_id=door_id)
