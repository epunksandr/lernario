from sqlalchemy import Column, Integer, Date, ForeignKey
from db.db import Base

class Abwesenheit(Base):
    __tablename__ = "abwesenheiten"

    abwesenheit_id = Column(Integer, primary_key=True)
    schueler_id = Column(Integer, ForeignKey("schueler.schueler_id", ondelete="CASCADE"), nullable=False)
    datum = Column(Date, nullable=False)
