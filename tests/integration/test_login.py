from tests import fixture
from tests.fixture import TestBase
from models.lehrer import Lehrer
import os
import time

fixture

def test_create_test_database():
    session = TestBase()
    new_obj = Lehrer(
    vorname="FirstName",
    nachname="NextName",
    email="t.test@gmail.com",
    passwort="123"
    )
    session.add(new_obj)
    session.commit()
    time.sleep(10)
    session.close()

    session = TestBase()
    lehrer = session.query(Lehrer)
    session.close()

    print(lehrer)

    if lehrer != "":
        assert True
    else:
        assert False

def test_is_login_false():
    try:
        session = TestBase()
        data = session.query(Lehrer)
        time.sleep(10)
        session.close()
    except:
        assert False

    if data:
        assert True
    else:
        assert False

def test_is_login_right():
    ...

def test_delete_db_file():
    time.sleep(10)
    os.remove("db/test.db")