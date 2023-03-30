from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_Child
from src.schemas import schem_Child
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Ребенок

@rout.post("/child", response_model=schem_Child.Child)
async def create_child(child: schem_Child.ChildCreate, db: Session = Depends(get_db)):

    db_child = cr_Child.get_child_group(db, group_id=child.group_id)
    if not db_child:
        raise HTTPException(status_code=404, detail="Данной группы не существует")
    
    return cr_Child.create_child(db=db, child=child)


@rout.get("/childs/group/{group_id}", response_model=list[schem_Child.Child])
async def get_childs_by_group(group_id: int, db: Session = Depends(get_db)):

    db_child_by_group = cr_Child.get_childs_by_group(db, group_id=group_id)
    if not db_child_by_group:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_child_by_group

@rout.get("/child/{child_id}", response_model=schem_Child.Child)
async def get_child(child_id: int, db: Session = Depends(get_db)):

    db_child = cr_Child.get_child(db, child_id=child_id)
    if not db_child:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_child

@rout.get("/childs", response_model=list[schem_Child.Child])
async def read_childs(skip: int=0, limit:int=100, db: Session = Depends(get_db)):

    return cr_Child.read_childs(db, skip=skip, limit=limit)

@rout.put("/child/{child_id}", response_model=schem_Child.Child)
async def edit_child(child: schem_Child.ChildUpdate, child_id: int, db: Session = Depends(get_db)):

    db_child = cr_Child.get_child_group(db, group_id=child.group_id)
    if not db_child:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    db_child = cr_Child.get_child(db, child_id=child_id)
    if not db_child:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    return cr_Child.update_child(db, child=child, child_id=child_id)

@rout.delete("/child/{child_id}", response_model=schem_Child.Child)
async def delete_child(child_id: int, db: Session = Depends(get_db)):

    db_child = cr_Child.get_child(db, child_id=child_id)
    if not db_child:
        raise HTTPException(status_code=404, detail="Невозможно удалить несуществующую запись")
    return cr_Child.delete_child(db, child_id=child_id)


