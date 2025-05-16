
from db.db import SessionLocal
from models.klassen import Klasse

class KlasseBaseService:
    def erstelle_klasse(self, klassenname):
        session = SessionLocal()
        new_obj = Klasse(klassenname)
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_klasse(self, klasse_id):
        session = SessionLocal()
        obj = session.query(Klasse).filter_by(klasse_id=klasse_id).first()
        session.close()
        return obj
    
    def aktualisiere_klasse(self, klasse_id, klassenname):
        session = SessionLocal()
        obj = self.gib_klasse(klasse_id)
        obj.klassenname=klassenname

        session.commit()
        session.close()
    
    def loesche_klasse(self, klasse_id):
        session = SessionLocal()
        obj = self.gib_klasse(klasse_id)
        session.delete(obj)
        session.commit()
        session.close()
    