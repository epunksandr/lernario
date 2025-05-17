from sqlalchemy import Column, Integer, String, ForeignKey
from db.db import Base

class Klasse(Base):
    __tablename__ = "klassen"

    klasse_id = Column(Integer, primary_key=True)
    klassenname = Column(String, nullable=False)
    lehrer_id = Column(Integer, ForeignKey("lehrer.lehrer_id", ondelete="CASCADE"), nullable=False)