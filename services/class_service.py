from services.sqllite_db import query_db

def add_class(klassenname: str):
    query_db("""
        INSERT INTO klassen (klassenname)
        VALUES (?)
    """, (klassenname,), commit=True)

def delete_class(class_id: int):
    query_db("""
        DELETE FROM klassen WHERE klasse_id = ?
        """, (class_id, ), commit=True)

def get_all_classes_with_students_count():
    query = """
        SELECT k.klasse_id, k.klassenname, COUNT(s.schueler_id) AS schueler_anzahl
        FROM klassen k
        LEFT JOIN schueler s ON s.klasse_id = k.klasse_id
        GROUP BY k.klasse_id, k.klassenname
    """
    result = query_db(query)
    return result

def get_all_classnames():
    return query_db("SELECT klassenname FROM klassen")

def gib_alle_klassen():
    return query_db("SELECT klasse_id, klassenname FROM klassen")

def gib_klassen_von_lehrer(lehrer_id: int):
    return query_db("""
        select klassen.klasse_id, klassen.klassenname from klassen
            join unterrichte on klassen.klasse_id = unterrichte.klasse_id
        where lehrer_id = ?
    """, (lehrer_id, ))

def gib_klassenanzahl(lehrer_id: int) -> int:
    result = query_db("""
    select COUNT(*) as klassenanzahl from unterrichte
    where lehrer_id = ?;
    """, (lehrer_id, ))
    return result[0]["klassenanzahl"]