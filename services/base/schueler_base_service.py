
from db.db import SessionLocal
from models.schueler import Schueler
from abc import ABC, abstractmethod

class SchuelerBaseService(ABC):

    @abstractmethod
    def gib_alle_schueler_von_lehrer(self, lehrer_id):
        pass

    def erstelle_schueler(self, klasse_id, vorname, nachname):
        session = SessionLocal()
        new_obj = Schueler(klasse_id=klasse_id, vorname=vorname, nachname=nachname)
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_schueler(self, schueler_id):
        session = SessionLocal()
        obj = session.query(Schueler).filter_by(schueler_id=schueler_id).first()
        session.close()
        return obj
    
    def aktualisiere_schueler(self, schueler_id, klasse_id, vorname, nachname):
        session = SessionLocal()
        obj = self.gib_schueler(schueler_id)
        klasse_id=klasse_id
        vorname=vorname
        nachname=nachname

        session.commit()
        session.close()
    
    def loesche_schueler(self, schueler_id):
        session = SessionLocal()
        obj = self.gib_schueler(schueler_id)
        session.delete(obj)
        session.commit()
        session.close()
    