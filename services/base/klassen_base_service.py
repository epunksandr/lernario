
from db.db import SessionLocal
from models.klassen import Klasse

class KlassenBaseService:
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
        obj = session.query(Klasse).filter_by(klasse_id=klasse_id, lehrer_id=lehrer_id).first()
        obj.klassenname=klassenname
        lehrer_id=lehrer_id

        session.commit()
        session.close()
    
    def loesche_klasse(self, klasse_id):
        session = SessionLocal()
        obj = self.gib_klasse(klasse_id)
        session.delete(obj)
        session.commit()
        session.close()
    