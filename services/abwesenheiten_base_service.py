
from db.db import SessionLocal
from models.abwesenheiten import Abwesenheit

class AbwesenheitBaseService:
    def erstelle_abwesenheit(self, schueler_id ,datum):
        session = SessionLocal()
        new_obj = Abwesenheit(schueler_id ,datum)
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_abwesenheit(self, abwesenheit_id):
        session = SessionLocal()
        obj = session.query(Abwesenheit).filter_by(abwesenheit_id=abwesenheit_id).first()
        session.close()
        return obj
    
    def aktualisiere_abwesenheit(self, abwesenheit_id, schueler_id ,datum):
        session = SessionLocal()
        obj = self.gib_abwesenheit(abwesenheit_id)
        obj.schueler_id=schueler_id
        obj.datum=datum

        session.commit()
        session.close()
    
    def loesche_abwesenheit(self, abwesenheit_id):
        session = SessionLocal()
        obj = self.gib_abwesenheit(abwesenheit_id)
        session.delete(obj)
        session.commit()
        session.close()
    