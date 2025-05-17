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

    def get_all_classnames(self):
        return query_db("SELECT klassenname FROM klassen")

    def gib_alle_klassen(self):
        return query_db("SELECT klasse_id, klassenname FROM klassen")

    def gib_klassen_von_lehrer(self, lehrer_id: int):
        return query_db("""
            select klassen.klasse_id, klassen.klassenname from klassen
                join unterrichte on klassen.klasse_id = unterrichte.klasse_id
            where lehrer_id = ?
        """, (lehrer_id,))

    def gib_klassenanzahl(self, lehrer_id: int) -> int:
        session = SessionLocal()
        klassenanzahl = session.query(func.count()).filter(Klasse.lehrer_id == lehrer_id).scalar()
        session.close()
        return klassenanzahl