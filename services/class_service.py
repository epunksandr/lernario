import sqlite3

from flask import jsonify


def get_db_connection():
    conn = sqlite3.connect('data/lernario.db')  # SQLite Datenbankdatei
    conn.row_factory = sqlite3.Row  # Um auf die Zeilen wie Dictionaries zugreifen zu können
    return conn

def add_class(classname: str) -> bool:
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO classes (classname, enrollment_year) VALUES (?, ?)", (classname, "2024"))
        connection.commit()
        return True
    except sqlite3.Error as e:
        print(f"Fehler beim Hinzufügen der Klasse: {e}")
        return False
    finally:
        connection.close()

def delete_class(class_id: int) -> bool:
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM classes WHERE class_id = ?", (class_id,))
        connection.commit()
        return cursor.rowcount > 0  # Gibt True zurück, wenn eine Zeile gelöscht wurde
    except sqlite3.Error as e:
        print(f"Fehler beim Löschen der Klasse: {e}")
        return False
    finally:
        connection.close()

def get_all_classes_with_students_count():
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT klassen.klasse_id, klassen.klassenname, COUNT(schueler.schueler_id) AS student_count
            FROM klassen
            LEFT JOIN schueler ON klassen.klasse_id = schueler.schueler_id
            GROUP BY klassen.klasse_id
        """)
        data = cursor.fetchall()
        print(data)
        return data
    except sqlite3.Error as e:
        print(f"Fehler beim Abrufen der Klassen mit Schülerzahl: {e}")
        return None
    finally:
        connection.close()

def get_all_classnames():
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT classname FROM classes")
        classes = cursor.fetchall()
        return [row['classname'] for row in classes]  # Gibt nur die Klassennamen zurück
    except sqlite3.Error as e:
        print(f"Fehler beim Abrufen der Klassennamen: {e}")
        return None
    finally:
        connection.close()