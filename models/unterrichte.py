from sqlalchemy import Column, Integer, ForeignKey
from db.db import Base

class Unterricht(Base):
    __tablename__ = "unterrichte"

    unterricht_id = Column(Integer, primary_key=True)
    lehrer_id = Column(Integer, ForeignKey("lehrer.lehrer_id", ondelete="CASCADE"), nullable=False)
    fach_id = Column(Integer, ForeignKey("faecher.fach_id", ondelete="CASCADE"), nullable=False)
    klasse_id = Column(Integer, ForeignKey("klassen.klasse_id", ondelete="CASCADE"), nullable=False)
