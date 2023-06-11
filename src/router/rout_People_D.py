from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_People_Door
from src.schemas import schem_People_Door
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# #Человек-дверь

@rout.post("/people_door")
async def create_PD(pd: schem_People_Door.PDCreate, db: Session = Depends(get_db)):

    db_PD_by_people = cr_People_Door.get_PD_people(db, people_id=pd.people_id)
    if not db_PD_by_people: 
        raise HTTPException(status_code=404, detail="Запись (П) отсутствует")

    db_PD_by_door = cr_People_Door.get_PD_door(db, door_id=pd.door_id)
    if not db_PD_by_door: 
        raise HTTPException(status_code=404, detail="Запись (Д) отсутствует")
    

    one_PD = cr_People_Door.get_PD_by_p_d(db, people_id=pd.people_id, door_id=pd.door_id)

    if one_PD:
        raise HTTPException(status_code=404, detail="Дублирующуяся запись")
    
    return cr_People_Door.create_PD(db=db, people_id=pd.people_id, door_id=pd.door_id)


@rout.get("/people_door/{people_door_id}", response_model=schem_People_Door.PD)
async def get_people_door(people_door_id: int, db: Session = Depends(get_db)):

    db_people_door = cr_People_Door.get_PD(db, PD_id=people_door_id)
    if not db_people_door:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_people_door

@rout.get("/people_door/people/{people_id}", response_model=list[schem_People_Door.PD])
async def get_people_door_by_p(people_id: int, db: Session = Depends(get_db)):

    db_people_door = cr_People_Door.get_PD_by_people(db, people_id=people_id)
    if not db_people_door:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_people_door

@rout.get("/people_door/door/{door_id}", response_model=list[schem_People_Door.PD])
async def get_people_door_by_d(door_id: int, db: Session = Depends(get_db)):

    db_people_door = cr_People_Door.get_PD_by_door(db, door_id=door_id)
    if not db_people_door:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_people_door


@rout.get("/people_doors", response_model=list[schem_People_Door.PD])
async def read_people_doors(skip:int=0, limit:int=100, db: Session = Depends(get_db)):

    return cr_People_Door.read_PDs(db, skip=skip, limit=limit)


@rout.put("/people_door/{people_door_id}")
async def edit_people_door(pd: schem_People_Door.PDUpdate, people_door_id, db: Session = Depends(get_db)):

    db_PD = cr_People_Door.get_PD(db, PD_id=people_door_id)
    if not db_PD:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    
    db_PD_by_people = cr_People_Door.get_PD_people(db, people_id=pd.people_id)
    if not db_PD_by_people: 
        raise HTTPException(status_code=404, detail="Запись (П) отсутствует")

    db_PD_by_door = cr_People_Door.get_PD_door(db, door_id=pd.door_id)
    if not db_PD_by_door: 
        raise HTTPException(status_code=404, detail="Запись (Д) отсутствует")
    

    one_PD = cr_People_Door.get_PD_by_p_d(db, people_id=pd.people_id, door_id=pd.door_id)

    if one_PD:
        raise HTTPException(status_code=404, detail="Дублирующуяся запись")
    
    return cr_People_Door.update_PD(db, pd=pd, PD_id=people_door_id)

@rout.delete("/people_door/{people_door_id}")
async def delete_people_door(people_door_id: int, db: Session = Depends(get_db)):

    db_people_door = cr_People_Door.get_PD(db, PD_id=people_door_id)
    if not db_people_door:
        raise HTTPException(status_code=404, detail="Невозможно удалить несуществующую запись")
    
    return cr_People_Door.delete_PD(db, PD_id=people_door_id)

