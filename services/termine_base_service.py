
from db.db import SessionLocal
from models.termine import Termin

class TermineBaseService:
    def erstelle_termin(self, termin_name, datum, klasse_id):
        session = SessionLocal()
        new_obj = Termin(termin_name=termin_name, datum=datum, klasse_id=klasse_id)
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_termin(self, termin_id):
        session = SessionLocal()
        obj = session.query(Termin).filter_by(termin_id=termin_id).first()
        session.close()
        return obj
    
    def aktualisiere_termin(self, termin_id, termin_name, datum, klasse_id):
        session = SessionLocal()
        obj = self.gib_termin(termin_id)
        termin_name=termin_name
        datum=datum
        klasse_id=klasse_id

        session.commit()
        session.close()
    
    def loesche_termin(self, termin_id):
        session = SessionLocal()
        obj = self.gib_termin(termin_id)
        session.delete(obj)
        session.commit()
        session.close()
    