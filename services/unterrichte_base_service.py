
from db.db import SessionLocal
from models.unterrichte import Unterricht

class UnterrichteBaseService:
    def erstelle_unterricht(self, lehrer_id, fach_id, klasse_id):
        session = SessionLocal()
        new_obj = Unterricht(lehrer_id=lehrer_id, fach_id=fach_id, klasse_id=klasse_id)
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_unterricht(self, unterricht_id):
        session = SessionLocal()
        obj = session.query(Unterricht).filter_by(unterricht_id=unterricht_id).first()
        session.close()
        return obj
    
    def aktualisiere_unterricht(self, unterricht_id, lehrer_id, fach_id, klasse_id):
        session = SessionLocal()
        obj = self.gib_unterricht(unterricht_id)
        lehrer_id=lehrer_id
        fach_id=fach_id
        klasse_id=klasse_id

        session.commit()
        session.close()
    
    def loesche_unterricht(self, unterricht_id):
        session = SessionLocal()
        obj = self.gib_unterricht(unterricht_id)
        session.delete(obj)
        session.commit()
        session.close()
    