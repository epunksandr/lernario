from sqlalchemy import Column, Integer, String
from db.db import Base
import hashlib

class Lehrer(Base):
    __tablename__ = "lehrer"

    lehrer_id = Column(Integer, primary_key=True)
    vorname = Column(String, nullable=False)
    nachname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    passwort_hash = Column(String, nullable=False)

    def __init__(self, vorname, nachname, email, passwort):
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
        self.passwort_hash = self.hash_passwort(passwort)

    def check_passwort(self, passwort) -> bool:
        passwort_hash = self.hash_passwort(passwort)
        if passwort_hash == self.passwort_hash:
            return True
        else:
            return False

    def hash_passwort(self, passwort):
        return hashlib.sha512(passwort.encode()).hexdigest()