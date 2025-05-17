
from db.db import SessionLocal
from models.lehrer import Lehrer

class LehrerBaseService:
    def erstelle_lehrer(self, vorname, nachname, email, passwort_hash):
        session = SessionLocal()
        new_obj = Lehrer(vorname=vorname, nachname=nachname, email=email, passwort_hash=passwort_hash)
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_lehrer(self, lehrer_id):
        session = SessionLocal()
        obj = session.query(Lehrer).filter_by(lehrer_id=lehrer_id).first()
        session.close()
        return obj
    
    def aktualisiere_lehrer(self, lehrer_id, vorname, nachname, email, passwort_hash):
        session = SessionLocal()
        obj = self.gib_lehrer(lehrer_id)
        vorname=vorname
        nachname=nachname
        email=email
        passwort_hash=passwort_hash

        session.commit()
        session.close()
    
    def loesche_lehrer(self, lehrer_id):
        session = SessionLocal()
        obj = self.gib_lehrer(lehrer_id)
        session.delete(obj)
        session.commit()
        session.close()
    