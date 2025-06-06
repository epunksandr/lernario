from abc import ABC

from db.db import SessionLocal
from models.lehrer import Lehrer
from services.base.lehrer_base_service import LehrerBaseService


class LehrerService(LehrerBaseService):

    def gib_alle_lehrer_von_lehrer(self, lehrer_id):
        pass

    def login_user(self, email, password) -> int:
        session = SessionLocal()
        lehrer = session.query(Lehrer).filter_by(email=email).first()

        if not lehrer:
            return 0

        if lehrer.check_passwort(password):
            return lehrer.lehrer_id
        else:
            return 0

    def register_user(self, vorname, nachname, email, password, session = SessionLocal()):

        session
        neuer_lehrer = Lehrer(
            vorname=vorname,
            nachname=nachname,
            email=email,
            passwort=password
        )
        session.add(neuer_lehrer)
        session.commit()
        session.close()
        return True
