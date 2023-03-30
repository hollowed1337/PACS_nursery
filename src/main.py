from fastapi import Depends, FastAPI
from src.database import SessionLocal
from src.router import rout_Role, rout_Card, rout_People, rout_Door, rout_Cab, rout_Child, rout_Group, rout_People_G, rout_People_D, rout_People_Ch, rout_Reader

app = FastAPI()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(rout_Role.rout, tags=["role"])
app.include_router(rout_Card.rout, tags=["card"])
app.include_router(rout_People.rout, tags=["people"])
app.include_router(rout_Door.rout, tags=["door"])
app.include_router(rout_Cab.rout, tags=["cab"])
app.include_router(rout_Child.rout, tags=["child"])
app.include_router(rout_Group.rout, tags=["group"])
app.include_router(rout_Reader.rout, tags=["reader"])
app.include_router(rout_People_G.rout, tags=["people_group"])
app.include_router(rout_People_Ch.rout, tags=["people_child"])
app.include_router(rout_People_D.rout, tags=["people_door"])