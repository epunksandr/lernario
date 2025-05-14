from flask import jsonify

from services.sqllite_db import query_db


def loesche_schueler(schueler_id: int):
    query_db("DELETE FROM schueler WHERE schueler_id=?;", (schueler_id, ), commit=True)

def gib_alle_schueler_mit_grundinformationen():
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


def gib_abwesenheiten_von_dieser_woche():
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