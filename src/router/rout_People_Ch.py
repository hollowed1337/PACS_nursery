from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_People_Child
from src.schemas import schem_People_Child
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#Человек-ребенок

@rout.post("/people_child")
async def create_PCh(pch: schem_People_Child.PChCreate, db: Session = Depends(get_db)):


    db_PCh_by_people = cr_People_Child.get_PCh_people(db, people_id=pch.people_id)
    if not db_PCh_by_people: 
        raise HTTPException(status_code=404, detail="Запись (П) отсутствует")

    db_PCh_by_child = cr_People_Child.get_PCh_child(db, child_id=pch.child_id)
    if not db_PCh_by_child: 
        raise HTTPException(status_code=404, detail="Запись (Ч) отсутствует")
    

    one_PCh = cr_People_Child.get_PCh_by_pch(db, child_id=pch.child_id, people_id=pch.people_id)
    if one_PCh:
        raise HTTPException(status_code=404, detail="Дублирующуяся запись")
    
    return cr_People_Child.create_PCh(db=db, people_id=pch.people_id, child_id=pch.child_id)


@rout.get("/people_child/{people_child_id}", response_model=schem_People_Child.PCh)
async def get_people_child(people_child_id: int, db: Session = Depends(get_db)):

    db_people_child = cr_People_Child.get_PCh(db, people_child_id=people_child_id)
    if not db_people_child:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_people_child

@rout.get("/people_child/people/{people_id}", response_model=list[schem_People_Child.PCh])
async def get_people_child_by_p(people_id: int, db: Session = Depends(get_db)):

    db_people_child = cr_People_Child.get_PCh_by_people(db, people_id=people_id)
    if not db_people_child:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_people_child

@rout.get("/people_child/child/{child_id}", response_model=list[schem_People_Child.PCh])
async def get_people_child_by_ch(child_id: int, db: Session = Depends(get_db)):

    db_people_child = cr_People_Child.get_PCh_by_child(db, child_id=child_id)
    if not db_people_child:
        raise HTTPException(status_code=404, detail="Записи не существует")
    
    return db_people_child


@rout.get("/people_childs", response_model=list[schem_People_Child.PCh])
async def read_people_childs(skip:int=0, limit:int=100, db: Session = Depends(get_db)):

    return cr_People_Child.read_PChs(db, skip=skip, limit=limit)


@rout.put("/people_child/{people_child_id}")
async def edit_people_child(pch: schem_People_Child.PChUpdate, people_child_id, db: Session = Depends(get_db)):

    db_PCh = cr_People_Child.get_PCh(db, people_child_id=people_child_id)
    if not db_PCh:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    
    db_PCh_by_people = cr_People_Child.get_PCh_people(db, people_id=pch.people_id)
    if not db_PCh_by_people: 
        raise HTTPException(status_code=404, detail="Запись (П) отсутствует")

    db_PCh_by_child = cr_People_Child.get_PCh_child(db, child_id=pch.child_id)
    if not db_PCh_by_child: 
        raise HTTPException(status_code=404, detail="Запись (Ч) отсутствует")
    
    one_PCh = cr_People_Child.get_PCh_by_pch(db, child_id=pch.child_id, people_id=pch.people_id)
    if one_PCh:
        raise HTTPException(status_code=404, detail="Дублирующуяся запись")
    
    return cr_People_Child.update_PCh(db=db, pch=pch, people_child_id=people_child_id)

@rout.delete("/people_child/{people_child_id}")
async def delete_people_child(people_child_id: int, db: Session = Depends(get_db)):

    db_people_child = cr_People_Child.get_PCh(db, people_child_id=people_child_id)
    if not db_people_child:
        raise HTTPException(status_code=404, detail="Невозможно удалить несуществующую запись")
    
    return cr_People_Child.delete_PCh(db, people_child_id=people_child_id)



