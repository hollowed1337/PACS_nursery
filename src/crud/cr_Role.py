from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_Role

def create_role(db: Session, role: schem_Role.RoleCreate):
    
    db_role = BaseModel.Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return {
        "status": "Успешно создано",
        "data": db_role
        }


def get_role(db: Session, role_id: int):
    
    return db.query(BaseModel.Role).filter(BaseModel.Role.id == role_id).first()

def get_role_by_name(db: Session, name: str):
    
    return db.query(BaseModel.Role).filter(BaseModel.Role.name == name).all()

def read_roles(db: Session, skip: int = 0, limit: int = 100):
    
    return db.query(BaseModel.Role).offset(skip).limit(limit).all()


def update_role(db: Session, role_id: int, role: schem_Role.RoleUpdate):

    db.query(BaseModel.Role).filter(BaseModel.Role.id == role_id).update(
        {
        BaseModel.Role.name: role.name
        }, synchronize_session="fetch"
    )
    db.commit()
    return {
        "status": f"Запись {role_id} изменена",
        "data" : db.query(BaseModel.Role).filter(BaseModel.Role.id == role_id).first()
        } 
    
    
def delete_role(db: Session, role_id: int):

    db_role = db.query(BaseModel.Role).filter(BaseModel.Role.id == role_id).first()
    db.delete(db_role)
    db.commit()
    return {
        "status": f"Запись {role_id} удалена",
        "data": db_role
        }
    