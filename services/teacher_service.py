from services.sqllite_db import query_db
import hashlib

def login_user(email, password):
    lehrer_id_json = query_db("""
        SELECT lehrer_id from lehrer
        where email == ?
    """, (email, ))

    try:
        lehrer_id = lehrer_id_json[0]["lehrer_id"]
    except:
        return None

    right_password_json = query_db("""
        SELECT passwort from lehrer
        where lehrer_id == ?
    """, (lehrer_id, ))
    try:
        right_password = right_password_json[0]["passwort"]
    except:
        return None

    password = hashlib.sha512(password.encode()).hexdigest()
    if right_password == password:
        return { "lehrer_id": lehrer_id }
    else:
        return None

def gib_lehrer(lehrer_id: int):
    result = query_db("""
        select * from lehrer
        where lehrer_id == ?
    """, (lehrer_id, ))
    return result


def register_user(vorname, nachname, email, password) -> bool:
    password = hashlib.sha512(password.encode()).hexdigest()

    result = query_db("""
    INSERT INTO lehrer (vorname, nachname, email, passwort)
    VALUES (?,?,?,?)
    """, (vorname, nachname, email, password, ), commit=True)
    print(result)
    return result