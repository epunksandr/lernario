from tests import fixture
from sqlalchemy import Column, Integer, String, ForeignKey
from services.lehrer_service import LehrerService

fixture
lehrerService = LehrerService()

def test_write_data_in_table():
    assert True