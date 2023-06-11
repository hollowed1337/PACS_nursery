from fastapi import Depends, HTTPException, APIRouter, Path
from sqlalchemy.orm import Session
from src.crud import cr_Role
from src.schemas import schem_Role
from src.database import SessionLocal

rout = APIRouter()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@rout.post("/role")
async def create_role(role: schem_Role.RoleCreate, db: Session = Depends(get_db)):
    
    db_role = cr_Role.get_role_by_name(db, name=role.name)
    if db_role:
        raise HTTPException(status_code=400, detail="Запись уже существует")
    
    return cr_Role.create_role(db=db, role=role)

@rout.get("/role/{role_id}", response_model=schem_Role.Role)
async def get_role(role_id:int, db: Session = Depends(get_db)):

    db_role = cr_Role.get_role(db, role_id=role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Записи не существует")
    return db_role


@rout.get("/roles", response_model=list[schem_Role.Role])
async def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    return cr_Role.read_roles(db, skip=skip, limit=limit)

@rout.put("/role/{role_id}")
def edit_role(role: schem_Role.RoleUpdate, role_id: int, db: Session = Depends(get_db)):

    db_role = cr_Role.get_role_by_name(db, name=role.name)
    if db_role:
        raise HTTPException(status_code=400, detail="Название роли занято")
    
    db_role = cr_Role.get_role(db, role_id=role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Невозможно изменить несуществующую запись")
    return cr_Role.update_role(db, role_id=role_id, role=role)


@rout.delete("/role/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):

    db_role = cr_Role.get_role(db, role_id=role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Невозможно удалить несуществующую запись")
    return cr_Role.delete_role(db, role_id=role_id)
