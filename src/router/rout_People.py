
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_People
from src.schemas import schem_People
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#Человек

@rout.post("/people")
def create_people(people: schem_People.PeopleCreate, db: Session = Depends(get_db)):

    db_peoples_by_role = cr_People.get_peoples_role(db, role_id=people.role_id)
    if not db_peoples_by_role:
        raise HTTPException(status_code=404, detail="Невозможно создать запись с несуществующей ролью")
    
    db_people_by_phone = cr_People.get_people_by_phone(db, phone=people.phone)
    if db_people_by_phone:
        raise HTTPException(status_code=404, detail="Данный номер телефона имеет другой человек")
    
    return cr_People.create_people(db=db, people=people, role_id=people.role_id)


@rout.get("/people/{people_id}", response_model=schem_People.People)
async def get_people(people_id: int, db: Session = Depends(get_db)):

    db_people = cr_People.get_people(db, people_id=people_id)
    if not db_people:
        raise HTTPException(status_code=404, detail="Такого человека не существует")
    return db_people


@rout.get("/peoples", response_model=list[schem_People.People])
async def read_peoples(skip: int =0, limit: int=100, db: Session = Depends(get_db)):

    return cr_People.read_peoples(db, skip=skip, limit=limit)


@rout.get("/peoples/role={role_id}", response_model=list[schem_People.People])
async def read_peoples_by_role(role_id:int, db: Session = Depends(get_db)):
    
    db_peoples_role = cr_People.get_peoples_role(db, role_id=role_id)
    if not db_peoples_role:
        raise HTTPException(status_code=404, detail="Такой роли не существует")
    return cr_People.get_peoples_by_role(db, role_id=role_id)

@rout.put("/people/{people_id}")
async def edit_people(people: schem_People.PeopleUpdate, people_id: int, db:Session = Depends(get_db)):

    db_people = cr_People.get_people(db, people_id=people_id)
    if not db_people:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    
    db_peoples_by_role = cr_People.get_peoples_role(db, role_id=people.role_id)
    if not db_peoples_by_role:
        raise HTTPException(status_code=404, detail="Невозможно поменять на несуществующую запись")
    
    db_people_by_phone = cr_People.get_people_by_phone_for_udp(db, phone=people.phone, people_id=people_id)
    if db_people_by_phone:
        raise HTTPException(status_code=404, detail="Данный номер телефона имеет другой человек")
    
    return cr_People.update_people(db, people_id=people_id, people=people) 


@rout.delete("/people/{people_id}")
async def delete_people(people_id:int, db: Session = Depends(get_db)):
    
    db_people = cr_People.get_people(db, people_id=people_id)
    if not db_people:
        raise HTTPException(status_code=404, detail="Невозможно удалить несуществующую запись")
    
    return cr_People.delete_people(db, people_id=people_id)
