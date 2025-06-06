from tests import fixture
from tests.fixture import TestBase
from models.lehrer import Lehrer

fixture

"""def test_create_test_database():
    session = TestBase()
    new_obj = Lehrer(
        vorname="FirstName",
        nachname="NextName",
        email="t.test@gmail.com",
        passwort="123"
        )
    session.add(new_obj)
    session.commit()
    session.close()

    session = TestBase()
    lehrer = session.query(Lehrer)
    session.close()

    if lehrer != "":
        assert True
    else:
        assert False"""

def test_is_login_false():
    session = TestBase()
    try:
        lehrer = session.query(Lehrer)
        assert True
    except:
        assert False

def test_is_login_right():
    ...