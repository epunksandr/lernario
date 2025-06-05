
from db.db import SessionLocal
from models.klassen import Klasse
from abc import ABC, abstractmethod

class KlassenBaseService(ABC):

    @abstractmethod
    def gib_alle_klassen_von_lehrer(self, lehrer_id):
        pass

    def erstelle_klasse(self, klassenname, lehrer_id):
        session = SessionLocal()
        new_obj = Klasse(klassenname=klassenname, lehrer_id=lehrer_id)
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_klasse(self, klasse_id):
        session = SessionLocal()
        obj = session.query(Klasse).filter_by(klasse_id=klasse_id).first()
        session.close()
        return obj
    
    def aktualisiere_klasse(self, klasse_id, klassenname, lehrer_id):
        session = SessionLocal()
        obj = self.gib_klasse(klasse_id)
        klassenname=klassenname
        lehrer_id=lehrer_id

        session.commit()
        session.close()
    
    def loesche_klasse(self, klasse_id):
        session = SessionLocal()
        obj = self.gib_klasse(klasse_id)
        session.delete(obj)
        session.commit()
        session.close()
    