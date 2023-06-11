from sqlalchemy import ForeignKey, Column, Integer, String, Date, DateTime, Boolean, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>"
    
#1
class People(BaseModel):
    __tablename__ = "peoples"
    __table_args__ = (
        CheckConstraint('role_id > 0'),
        )
    name = Column(String(50), nullable=True)
    phone = Column(String(11), unique=True, index=True, nullable=True)
    password = Column(String(100))
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="people")
    card = relationship("Card", back_populates="people")
    door_p = relationship("Door_People", back_populates="people")
    people_ch = relationship("People_Child", back_populates="people")
    group_p = relationship("Group_People", back_populates="people")

#2
class Card(BaseModel):
    __tablename__ = "cards"
    __table_args__ = (
        CheckConstraint('deactivate_date > activate_date'),
        CheckConstraint('people_id > 0'),
    )
    code = Column(String(20), unique=True, index=True, nullable=False)
    activate_date = Column(Date)
    deactivate_date = Column(Date)
    status = Column(Boolean, default=False)
    people_id = Column(Integer, ForeignKey("peoples.id"))

    people = relationship("People", back_populates="card")
    log = relationship("Log", back_populates="card")

#3
class Role(BaseModel):
    __tablename__ = "roles"

    name = Column(String(50), unique=True, index=True, nullable=False)

    people = relationship("People", back_populates="role")

#4
class Child(BaseModel):
    __tablename__ = "childs"
    __table_args__ = (
        CheckConstraint('group_id > 0'),
    )

    name = Column(String(50), nullable=False)
    birth_date = Column(Date)
    group_id = Column(Integer, ForeignKey("kid_groups.id"))
    door_id = Column(Integer, ForeignKey("doors.id"))

    kid_group = relationship("Kid_group", back_populates="child")
    people_ch = relationship("People_Child", back_populates="child")
    door = relationship("Door", back_populates="child")

#6
class Kid_group(BaseModel):
    __tablename__ = "kid_groups"
    __table_args__ = (
        CheckConstraint('cabinet_id > 0'),
    )

    name = Column(String(50), unique=True, index=True)
    cabinet_id = Column(Integer, ForeignKey("cabinets.id"))

    child = relationship("Child", back_populates="kid_group")
    cabinet = relationship("Cabinet", back_populates="kid_group")
    group_p = relationship("Group_People", back_populates="kid_group")

#5
class Cabinet(BaseModel):
    __tablename__ = "cabinets"

    num_cabinet = Column(String(3), unique=True, index=True, nullable=False)

    kid_group = relationship("Kid_group", back_populates="cabinet")
    door = relationship("Door", back_populates="cabinet")
    reader = relationship("Reader", back_populates="cabinet")

#9
class Door(BaseModel):
    __tablename__ = "doors"

    door_num = Column(String(3), unique=True, index=True, nullable=False)
    type_door = Column(String(10))
    cabinet_id = Column(Integer, ForeignKey("cabinets.id"))

    door_p = relationship("Door_People", back_populates="door")
    cabinet = relationship("Cabinet", back_populates="door")
    child = relationship("Child", back_populates="door")

class Reader(BaseModel):
    __tablename__ = "readers"

    serial_num = Column(String(10), unique=True, index=True)
    cabinet_id = Column(Integer, ForeignKey("cabinets.id"))

    cabinet = relationship("Cabinet", back_populates="reader")
    log = relationship("Log", back_populates="reader")


class Log(BaseModel):
    __tablename__ = "logs"

    id_reader = Column(Integer, ForeignKey("readers.id"))
    id_card = Column(Integer, ForeignKey("cards.id"))
    date = Column(DateTime(6))

    reader = relationship("Reader", back_populates="log")
    card = relationship("Card", back_populates="log")

#7
class Group_People(BaseModel):
    __tablename__ = "group_people"
    __table_args__ = (
        CheckConstraint('group_id > 0'),
        CheckConstraint('people_id > 0'),
    )
    group_id = Column(Integer, ForeignKey("kid_groups.id"))
    people_id = Column(Integer, ForeignKey("peoples.id"))

    kid_group = relationship("Kid_group", back_populates="group_p")
    people = relationship("People", back_populates="group_p")

#8
class People_Child(BaseModel):
    __tablename__ = "people_child"
    __table_args__ = (
        CheckConstraint('child_id > 0'),
        CheckConstraint('people_id > 0'),
    )
    child_id = Column(Integer, ForeignKey("kids.id"))
    people_id = Column(Integer, ForeignKey("peoples.id"))

    child = relationship("Child", back_populates="people_ch")
    people = relationship("People", back_populates="people_ch")

#10
class Door_People(BaseModel):
    __tablename__ = "door_people"
    __table_args__ = (
        CheckConstraint('door_id > 0'),
        CheckConstraint('people_id > 0'),
    )
    door_id = Column(Integer, ForeignKey("doors.id"))
    people_id = Column(Integer, ForeignKey("peoples.id"))

    door = relationship("Door", back_populates="door_p")
    people = relationship("People", back_populates="door_p")
