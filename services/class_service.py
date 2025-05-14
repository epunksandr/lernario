from services.sqllite_db import query_db

def add_class(classname: str):
    query_db("""
    INSERT INTO classes (classname, enrollment_year) VALUES (?, ?)
    """, (classname, "2024", ), commit=True)

def delete_class(class_id: int):
    query_db("""
        DELETE FROM klassen WHERE klasse_id = ?
        """, (class_id, ), commit=True)

def get_all_classes_with_students_count():
    return query_db("""
        select klassen.klasse_id, klassen.klassenname, COUNT(DISTINCT schueler.schueler_id) as schueler_anzahl from schueler
        join klassen on schueler.klasse_id = klassen.klasse_id
        group by klassen.klasse_id
    """)

def get_all_classnames():
    return query_db("SELECT classname FROM classes")

def gib_klassen_von_lehrer(lehrer_id: int):
    return query_db("""
        select klassen.klasse_id, klassen.klassenname from klassen
            join unterrichte on klassen.klasse_id = unterrichte.klasse_id
        where lehrer_id = ?
    """, (lehrer_id, ))