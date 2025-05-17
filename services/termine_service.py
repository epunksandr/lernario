from flask import jsonify

from services.sqllite_db import query_db
from services.termine_base_service import TermineBaseService


class TermineService(TermineBaseService):

    def gib_alle_termine(self):
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