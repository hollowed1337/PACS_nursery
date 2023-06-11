from fastapi import FastAPI, Depends
from src.database import SessionLocal
from src.router import rout_Role, rout_Card, rout_People, rout_Door, rout_Cab, rout_Child, rout_Group, rout_People_G, rout_People_D, rout_People_Ch, rout_Reader, rout_Log
from src.pages import cabinet, card, child, door, group, home, log, people_child, people_door, people_group, people, reader, role 
from src.auth import router

app = FastAPI()

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(rout_Log.rout, tags=["journal"])
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
app.include_router(home.router)
app.include_router(people.router)
app.include_router(cabinet.router)
app.include_router(card.router)
app.include_router(child.router)
app.include_router(door.router)
app.include_router(group.router)
app.include_router(log.router)
app.include_router(people_child.router)
app.include_router(people_door.router)
app.include_router(people_group.router)
app.include_router(reader.router)
app.include_router(role.router)
app.include_router(router.router)
