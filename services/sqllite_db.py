import sqlite3

from flask import jsonify

DB_PATH = 'data/lernario.db'

def query_db(query, params=(), commit=False):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row  # für Dict-ähnliche Zeilen
        cursor = conn.cursor()
        cursor.execute(query, params)
        if commit:
            conn.commit()
        data = cursor.fetchall()
        return [dict(row) for row in data]  # liefert Liste von Dicts