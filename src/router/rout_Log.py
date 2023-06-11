from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.crud import cr_Log
from src.schemas import schem_Log
from src.database import SessionLocal
from datetime import datetime, timedelta

rout = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Журнал



@rout.get("/log/{log_id}", response_model= schem_Log.Log)
async def get_log(log_id: int, db: Session = Depends(get_db)):
    
    return cr_Log.get_log(db, log_id=log_id)

@rout.get("/logs", response_model= list[schem_Log.Log])
async def read_logs(skip:int=0, limit:int=100, db: Session = Depends(get_db)):
    
    return cr_Log.read_logs(db, skip=skip, limit=limit)



@rout.get("/logs_between", response_model= list[schem_Log.Log])
async def between_time(start_dt: datetime, end_dt: datetime, skip:int=0, limit:int=20, db: Session = Depends(get_db)):
    
    return cr_Log.between_time(db, start_dt=start_dt, end_dt=end_dt, skip=skip, limit=limit)


@rout.get("/logs/people={people_id}")
async def read_logs_by_people(people_id: int, db: Session = Depends(get_db)):
    
    return cr_Log.read_logs_by_people(db, people_id=people_id)




@rout.get("/logs/child_door={door_id}")
async def read_logs_by_childDoor(door_id: int, start_dt: datetime, end_dt: datetime, skip:int=0, limit:int=20, db: Session = Depends(get_db)):
    

    return cr_Log.read_logs_by_door(db, door_id=door_id, start_dt=start_dt, end_dt=end_dt, skip=skip, limit=limit)