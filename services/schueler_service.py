from flask import jsonify, session
from sqlalchemy import func

from db.db import SessionLocal
from models.klassen import Klasse
from models.schueler import Schueler
from services.base.schueler_base_service import SchuelerBaseService

class SchuelerService(SchuelerBaseService):

    def gib_alle_schueler_mit_grundinformationen(self, lehrer_id):
        session = SessionLocal()
        schueler = (session.query(
            Schueler.schueler_id,
            Schueler.vorname,
            Schueler.nachname,
            Klasse.klassenname)
                    .join(Klasse, Schueler.klasse_id == Klasse.klasse_id)
                    .filter(Klasse.lehrer_id == lehrer_id)
                    .group_by(Schueler.schueler_id)
                    .all())
        session.close()
        return schueler

    def gib_schueleranzahl_von_lehrer(self, lehrer_id: int):
        session = SessionLocal()
        schueleranzahl = (session.query(func.count(Schueler.schueler_id))
                          .select_from(Klasse)
                          .join(Schueler, Schueler.klasse_id == Klasse.klasse_id)
                          .filter(Klasse.lehrer_id == lehrer_id)
                          .scalar()
                          )
        session.close()
        return schueleranzahl


