from sqlalchemy import Column, Integer, String, Date, ForeignKey
from db.db import Base

class Termin(Base):
    __tablename__ = "termine"

    termin_id = Column(Integer, primary_key=True)
    termin_name = Column(String, nullable=False)
    datum = Column(Date, nullable=False)
    klasse_id = Column(Integer, ForeignKey("klassen.klasse_id", ondelete="CASCADE"))
    beschreibung = Column(String)
