from flask import jsonify, session
from sqlalchemy import func

from db.db import SessionLocal
from models.klassen import Klasse
from models.unterrichte import Unterricht
from services.schueler_base_service import SchuelerBaseService
from services.sqllite_db import query_db
from models.schueler import Schueler
from models.abwesenheiten import Abwesenheit

class SchuelerService(SchuelerBaseService):
    def erstelle_schueler(self, vorname, nachname, klasse_id: None):
        query_db("""
            insert into schueler (vorname, nachname, klasse_id)
            values (?, ?, ?)
        """, (vorname, nachname, klasse_id), commit=True)

    def loesche_schueler(self, schueler_id: int):
        query_db("DELETE FROM schueler WHERE schueler_id=?;", (schueler_id,), commit=True)

    def gib_alle_schueler_mit_grundinformationen(self):
        data = query_db(
            """
            select
                schueler.schueler_id,
                schueler.vorname,
                schueler.nachname,
                klassen.klassenname,
                COUNT(DISTINCT abwesenheiten.abwesenheit_id) AS abwesenheiten,
                ROUND(AVG(noten.note), 1) AS notenschnitt
            from schueler
                left JOIN klassen ON schueler.klasse_id = klassen.klasse_id
                left JOIN abwesenheiten ON schueler.schueler_id = abwesenheiten.schueler_id
                left JOIN noten ON schueler.schueler_id = noten.schueler_id
            GROUP BY noten.schueler_id
        """)
        return data

    def gib_abwesenheiten_von_dieser_woche(self):
        session = SessionLocal()
        data = (
            session.query(
                Schueler.schueler_id,
                Schueler.vorname,
                Schueler.nachname,
                Klasse.klassenname,
                func.count(Abwesenheit.abwesenheit_id).label("abwesenheiten")
            )
            .join(Abwesenheit, Schueler.schueler_id == Abwesenheit.schueler_id)
            .join(Klasse, Schueler.klasse_id == Klasse.klasse_id)
            .group_by(Schueler.schueler_id)
            .all()
        )
        print(data)
        session.close()
        return data

    def gib_schueleranzahl_von_lehrer(self, lehrer_id: int):
        session = SessionLocal()
        schueleranzahl = (session.query(func.count(Schueler.schueler_id))
                          .select_from(Klasse)
                          .join(Schueler, Schueler.klasse_id == Klasse.klasse_id)
                          .join(Unterricht, Unterricht.klasse_id == Klasse.klasse_id)
                          .filter(Unterricht.lehrer_id == lehrer_id)
                          .scalar()
                          )
        session.close()
        return schueleranzahl


