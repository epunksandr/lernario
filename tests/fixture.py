from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

engine = create_engine("sqlite:///db/test.db", echo=True)

#Wichtig damit ondelete=cascade funktioniert
@event.listens_for(Engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

TestBase = sessionmaker(bind=engine)
Base = declarative_base()
class Klasse(Base):
    __tablename__ = "klassen"

    klasse_id = Column(Integer, primary_key=True)
    klassenname = Column(String, nullable=False)
Base.metadata.create_all(bind=engine)