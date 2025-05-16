from sqlalchemy import Column, Integer, Float, ForeignKey
from db.db import Base

class Note(Base):
    __tablename__ = "noten"

    note_id = Column(Integer, primary_key=True)
    schueler_id = Column(Integer, ForeignKey("schueler.schueler_id", ondelete="CASCADE"), nullable=False)
    unterricht_id = Column(Integer, ForeignKey("unterrichte.unterricht_id", ondelete="CASCADE"), nullable=False)
    note = Column(Float, nullable=False)
