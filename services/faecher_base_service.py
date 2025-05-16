
from db.db import SessionLocal
from models.faecher import Fach

class FachBaseService:
    def erstelle_fach(self, fach):
        session = SessionLocal()
        new_obj = Fach(fach)
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_fach(self, fach_id):
        session = SessionLocal()
        obj = session.query(Fach).filter_by(fach_id=fach_id).first()
        session.close()
        return obj
    
    def aktualisiere_fach(self, fach_id, fach):
        session = SessionLocal()
        obj = self.gib_fach(fach_id)
        obj.fach=fach

        session.commit()
        session.close()
    
    def loesche_fach(self, fach_id):
        session = SessionLocal()
        obj = self.gib_fach(fach_id)
        session.delete(obj)
        session.commit()
        session.close()
    