from gotrue import Session
from sqlalchemy import func

from models.klassen import Klasse
from models.unterrichte import Unterricht

from db.db import SessionLocal
from services.klassen_base_service import KlassenBaseService
from services.sqllite_db import query_db

class KlassenService(KlassenBaseService):

    def get_all_classes_with_students_count(self):
        query = """
            SELECT k.klasse_id, k.klassenname, COUNT(s.schueler_id) AS schueler_anzahl
            FROM klassen k
            LEFT JOIN schueler s ON s.klasse_id = k.klasse_id
            GROUP BY k.klasse_id, k.klassenname
        """
        result = query_db(query)
        return result

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
