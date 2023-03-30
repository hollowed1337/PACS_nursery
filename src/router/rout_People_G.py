from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_People_Group
from src.schemas import schem_People_Group
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Человек-группа

@rout.post("/people_group", response_model=schem_People_Group.PG)
async def create_PG(pg: schem_People_Group.PGCreate, db: Session = Depends(get_db)):


    db_PG_by_people = cr_People_Group.get_PG_people(db, people_id=pg.people_id)
    if not db_PG_by_people: 
        raise HTTPException(status_code=404, detail="Запись (П) отсутствует")

    db_PG_by_group = cr_People_Group.get_PG_group(db, group_id=pg.group_id)
    if not db_PG_by_group: 
        raise HTTPException(status_code=404, detail="Запись (Г) отсутствует")
    

    one_PG = cr_People_Group.get_PG_by_p_g(db, group_id=pg.group_id, people_id=pg.people_id)
    if one_PG:
        raise HTTPException(status_code=404, detail="Дублирующуяся запись")
    
    return cr_People_Group.create_PG(db=db, people_id=pg.people_id, group_id=pg.group_id)


@rout.get("/people_group/{people_group_id}", response_model=schem_People_Group.PG)
async def get_people_group(people_group_id: int, db: Session = Depends(get_db)):

    db_people_group = cr_People_Group.get_PG(db, PG_id=people_group_id)
    if not db_people_group:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_people_group


@rout.get("/people_group/people/{people_id}", response_model=list[schem_People_Group.PG])
async def get_people_child_by_p(people_id: int, db: Session = Depends(get_db)):

    db_people_group = cr_People_Group.get_PG_by_people(db, people_id=people_id)
    if not db_people_group:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_people_group

@rout.get("/people_group/group/{group_id}", response_model=list[schem_People_Group.PG])
async def get_people_group_by_g(group_id: int, db: Session = Depends(get_db)):

    db_people_group = cr_People_Group.get_PG_by_group(db, group_id=group_id)
    if not db_people_group:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_people_group


@rout.get("/people_groups", response_model=list[schem_People_Group.PG])
async def read_people_groups(skip:int=0, limit:int=100, db: Session = Depends(get_db)):

    return cr_People_Group.read_PGs(db, skip=skip, limit=limit)


@rout.put("/people_group/{people_group_id}", response_model=schem_People_Group.PG)
async def edit_people_child(pg: schem_People_Group.PGUpdate, people_group_id, db: Session = Depends(get_db)):


    one_PG = cr_People_Group.get_PG_by_p_g(db, group_id=pg.group_id, people_id=pg.people_id)
    if one_PG:
        raise HTTPException(status_code=404, detail="Дублирующуяся запись")
    
    db_PG = cr_People_Group.get_PG(db, PG_id= people_group_id)
    if not db_PG:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    

    db_PG_by_people = cr_People_Group.get_PG_people(db, people_id=pg.people_id)
    if not db_PG_by_people: 
        raise HTTPException(status_code=404, detail="Запись (П) отсутствует")

    db_PG_by_group = cr_People_Group.get_PG_group(db, group_id=pg.group_id)
    if not db_PG_by_group: 
        raise HTTPException(status_code=404, detail="Запись (Г) отсутствует")

    one_PG = cr_People_Group.get_PG_by_p_g(db, group_id=pg.group_id, people_id=pg.people_id)
    if one_PG:
        raise HTTPException(status_code=404, detail="Дублирующуяся запись")
    
    return cr_People_Group.update_PG(db=db, pg=pg, PG_id=people_group_id)

@rout.delete("/people_group/{people_group_id}", response_model=schem_People_Group.PG)
async def delete_people_group(people_group_id: int, db: Session = Depends(get_db)):

    db_people_group = cr_People_Group.get_PG(db, PG_id=people_group_id)
    if not db_people_group:
        raise HTTPException(status_code=404, detail="Невозможно удалить несуществующую запись")
    
    return cr_People_Group.delete_PG(db, PG_id=people_group_id)