import sqlite3

from flask import jsonify

DB_PATH = 'db/lernario.db'

def query_db(query, params=(), commit=False):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")#Wichtig damit ON DELETE CASCADE funktioniert
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, params)
        if commit:
            conn.commit()
        data = cursor.fetchall()
        return [dict(row) for row in data]