from sqlalchemy import Column, Integer, String, ForeignKey
from db.db import Base

class Schueler(Base):
    __tablename__ = "schueler"

    schueler_id = Column(Integer, primary_key=True)
    klasse_id = Column(Integer, ForeignKey("klassen.klasse_id", ondelete="CASCADE"), nullable=False)
    vorname = Column(String, nullable=False)
    nachname = Column(String, nullable=False)
