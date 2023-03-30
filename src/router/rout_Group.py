from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_Group
from src.schemas import schem_Group
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Группа

@rout.post("/group", response_model=schem_Group.Group)
async def create_group(group: schem_Group.GroupCreate, db: Session = Depends(get_db)):

    db_group_name = cr_Group.get_group_by_name(db, name=group.name)
    if db_group_name:
        raise HTTPException(status_code=400, detail="Название занято")
    
    db_group_by_cab = cr_Group.get_group_by_cab(db, cab_id=group.cabinet_id)
    if db_group_by_cab:
        raise HTTPException(status_code=400, detail="Данный кабинет уже закреплен за группой")
    
    db_group_cab = cr_Group.get_group_cab(db, cab_id=group.cabinet_id)
    if not db_group_cab:
        raise HTTPException(status_code=404, detail="Запись отсутствует")
    
    return cr_Group.create_group(db=db, group=group, cabinet_id=group.cabinet_id)

@rout.get("/group/{group_id}", response_model=schem_Group.Group)
async def get_group(group_id: int, db: Session = Depends(get_db)):

    db_group = cr_Group.get_group(db, group_id=group_id)
    if not db_group:
        raise HTTPException(status_code=404, detail="Записи не существует")
    return db_group

@rout.get("/group/cab/{cab_id}", response_model=list[schem_Group.Group])
async def get_group_by_cab(cab_id: int, db: Session = Depends(get_db)):

    db_group = cr_Group.get_group_by_cab(db, cab_id=cab_id)
    if not db_group:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_group


@rout.get("/groups", response_model=list[schem_Group.Group])
async def read_groups(skip:int=0, limit:int=100, db: Session = Depends(get_db)):

    return cr_Group.read_groups(db, skip=skip, limit=limit)

@rout.put("/group/{group_id}", response_model=schem_Group.Group)
async def edit_group(group: schem_Group.GroupUpdate, group_id: int, db: Session = Depends(get_db)):

    db_group_name = cr_Group.get_group_by_name(db, name=group.name)
    if db_group_name:
        raise HTTPException(status_code=400, detail="Название занято")
    
    db_group_by_cab = cr_Group.get_group_by_cab(db, cab_id=group.cabinet_id)
    if db_group_by_cab:
        raise HTTPException(status_code=400, detail="Другая группа уже базируется в этом кабинете")
    db_group_cab = cr_Group.get_group_cab(db, cab_id=group.cabinet_id)
    if not db_group_cab:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    
    db_group = cr_Group.get_group(db, group_id=group_id)
    if not db_group:
        raise HTTPException(status_code=404, detail="Записи не существует")

    return cr_Group.update_group(db, group_id=group_id, group=group)

@rout.delete("/group/{group_id}", response_model=schem_Group.Group)
async def delete_group(group_id: int, db: Session = Depends(get_db)):
        
    db_group = cr_Group.get_group(db, group_id=group_id)
    if not db_group:
        raise HTTPException(status_code=404, detail="Невозможно удалить отсутствующую запись")
    
    return cr_Group.delete_group(db, group_id=group_id)
