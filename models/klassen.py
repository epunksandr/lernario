from sqlalchemy import Column, Integer, String
from db.db import Base

class Klasse(Base):
    __tablename__ = "klassen"

    klasse_id = Column(Integer, primary_key=True)
    klassenname = Column(String, nullable=False)
