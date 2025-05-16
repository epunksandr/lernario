from sqlalchemy import Column, Integer, String
from db.db import Base

class Fach(Base):
    __tablename__ = "faecher"

    fach_id = Column(Integer, primary_key=True)
    fach = Column(String, nullable=False)
