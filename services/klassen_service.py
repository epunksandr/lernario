from gotrue import Session
from sqlalchemy import func

from models.klassen import Klasse
from db.db import SessionLocal
from models.schueler import Schueler
from services.base.klassen_base_service import KlassenBaseService


class KlassenService(KlassenBaseService):

    def gib_klassen_mit_schueleranzahl_von_lehrer(self, lehrer_id: int):
        session = SessionLocal()
        klassen = (session.query(Klasse.klasse_id, Klasse.klassenname, func.count(Schueler.schueler_id).label("schueler_anzahl"))
                   .join(Schueler, Klasse.klasse_id == Schueler.klasse_id)
                   .filter(Klasse.lehrer_id == lehrer_id)
                   .all())
        session.close()
        return klassen

    def gib_klassen_von_lehrer(self, lehrer_id: int):
        session = SessionLocal()
        klassen = session.query(Klasse).filter(Klasse.lehrer_id == lehrer_id).all()
        session.close()
        return klassen

    def gib_klassenanzahl(self, lehrer_id: int) -> int:
        session = SessionLocal()
        klassenanzahl = session.query(func.count()).filter(Klasse.lehrer_id == lehrer_id).scalar()
        session.close()
        return klassenanzahl
