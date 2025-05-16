from db.db import SessionLocal
from models.lehrer import Lehrer

def login_user(email, password) -> int:
    session = SessionLocal()
    lehrer = session.query(Lehrer).filter_by(email=email).first()

    if not lehrer:
        return 0

    if lehrer.check_passwort(password):
        return lehrer.lehrer_id
    else:
        return 0

def gib_lehrer(lehrer_id: int):
    session = SessionLocal()
    lehrer = session.query(Lehrer).filter_by(lehrer_id=lehrer_id).first()
    session.close()
    return lehrer

def register_user(vorname, nachname, email, password):

    session = SessionLocal()
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
