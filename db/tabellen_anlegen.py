from db.db import Base, engine

from models.klassen import Klasse
from models.lehrer import Lehrer
from models.schueler import Schueler
from models.termine import Termin

def tabellen_anlegen():
    Base.metadata.create_all(bind=engine)