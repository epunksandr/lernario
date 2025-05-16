
from db.db import SessionLocal
from models.noten import Note

class NoteBaseService:
    def erstelle_note(self, schueler_id ,unterricht_id ,note):
        session = SessionLocal()
        new_obj = Note(schueler_id ,unterricht_id ,note)
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_note(self, note_id):
        session = SessionLocal()
        obj = session.query(Note).filter_by(note_id=note_id).first()
        session.close()
        return obj
    
    def aktualisiere_note(self, note_id, schueler_id ,unterricht_id ,note):
        session = SessionLocal()
        obj = self.gib_note(note_id)
        obj.schueler_id=schueler_id
        obj.unterricht_id=unterricht_id
        obj.note=note

        session.commit()
        session.close()
    
    def loesche_note(self, note_id):
        session = SessionLocal()
        obj = self.gib_note(note_id)
        session.delete(obj)
        session.commit()
        session.close()
    