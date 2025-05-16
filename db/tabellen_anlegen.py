from db.db import Base, engine

from models.abwesenheiten import Abwesenheit
from models.faecher import Fach
from models.klassen import Klasse
from models.lehrer import Lehrer
from models.noten import Note
from models.schueler import Schueler
from models.termine import Termin
from models.unterrichte import Unterricht

def tabellen_anlegen():
    Base.metadata.create_all(bind=engine)
