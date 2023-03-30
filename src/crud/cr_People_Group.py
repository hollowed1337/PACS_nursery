from sqlalchemy.orm import Session
from src.model import BaseModel
from src.schemas import schem_People_Group



def create_PG(db: Session, people_id: int, group_id: int):

    db_PG = BaseModel.Group_People(people_id=people_id, group_id=group_id)
    db.add(db_PG)
    db.commit()
    db.refresh(db_PG)
    return db_PG


def get_PG(db: Session, PG_id: int):

    return db.query(BaseModel.Group_People).filter(BaseModel.Group_People.id == PG_id).first()

def get_PG_people(db: Session, people_id: int):

    return db.query(BaseModel.People).filter(BaseModel.People.id == people_id).all()


def get_PG_group(db: Session, group_id: int):

    return db.query(BaseModel.Kid_group).filter(BaseModel.Kid_group.id == group_id).all()


def get_PG_by_group(db: Session, group_id: int):

    return db.query(BaseModel.Group_People).filter(BaseModel.Group_People.group_id == group_id).all()


def get_PG_by_people(db: Session, people_id: int):

    return db.query(BaseModel.Group_People).filter(BaseModel.Group_People.people_id == people_id).all()

def get_PG_by_p_g(db: Session, people_id: int, group_id: int):

    return db.query(BaseModel.Group_People).filter(BaseModel.Group_People.people_id == people_id).filter(BaseModel.Group_People.group_id == group_id).first()


def read_PGs(db: Session, skip:int=0, limit:int=100):

    return db.query(BaseModel.Group_People).offset(skip).limit(limit).all()


def update_PG(db: Session, PG_id: int, pg: schem_People_Group.PGUpdate):

    db.query(BaseModel.Group_People).filter(BaseModel.Group_People.id == PG_id).update(
        {
        BaseModel.Group_People.people_id: pg.people_id, 
        BaseModel.Group_People.group_id: pg.group_id
        }, synchronize_session="fetch"
    )
    db.commit()
    return db.query(BaseModel.Group_People).filter(BaseModel.Group_People.id == PG_id).first()

def delete_PG(db: Session, PG_id: int):

    db_PG = db.query(BaseModel.Group_People).filter(BaseModel.Group_People.id == PG_id).first()
    db.delete(db_PG)
    db.commit()
    return db_PG