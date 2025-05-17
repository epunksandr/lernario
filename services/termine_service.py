from flask import jsonify, session

from db.db import SessionLocal
from models.klassen import Klasse
from models.termine import Termin
from services.sqllite_db import query_db
from services.termine_base_service import TermineBaseService
from datetime import date


class TermineService(TermineBaseService):

    def gib_termine(self, lehrer_id, limit=None):
        session = SessionLocal()
        termine = (session.query(Termin.termin_id, Termin.termin_name, Termin.datum, Klasse.klassenname)
                   .join(Klasse, Termin.klasse_id == Klasse.klasse_id)
                   .filter(Klasse.lehrer_id == lehrer_id)
                   .filter(Termin.datum >= date.today())
                   .order_by(Termin.datum)
                   .limit(limit)
                   .all())
        session.close()
        return termine
