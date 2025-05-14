from flask import jsonify

from services.sqllite_db import query_db


def loesche_schueler(schueler_id: int):
    query_db("DELETE FROM schueler WHERE schueler_id=?;", (schueler_id, ), commit=True)

def gib_alle_termine():
    data = query_db(
        """
        select
            termine.termin_name,
            termine.datum,
            ifnull(termine.beschreibung, '') AS beschreibung,
            klassen.klassenname
            from termine JOIN klassen ON termine.klasse_id = klassen.klasse_id
    """)
    return data

def neuer_termin(termin_name, datum, klasse_id=None, beschreibung=None):
    query_db(
        """
        insert into termine (termin_name, datum, klasse_id, beschreibung)
        values (?, ?, ?, ?)
    """, (termin_name, datum, klasse_id, beschreibung), commit=True)