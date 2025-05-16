from datetime import date
from db.db import SessionLocal
from models.klassen import Klasse
from models.schueler import Schueler
from models.abwesenheiten import Abwesenheit

session = SessionLocal()

# 1. Dummy-Klasse anlegen
klasse = Klasse(klassenname="10A")
session.add(klasse)
session.commit()  # jetzt hat klasse.klasse_id einen Wert

# 2. Schüler anlegen, der zur Klasse gehört
schueler = Schueler(
    vorname="Anna",
    nachname="Müller",
    klasse_id=klasse.klasse_id  # wichtig!
)
session.add(schueler)
session.commit()

# 3. Abwesenheit für diesen Schüler anlegen
abwesenheit = Abwesenheit(
    schueler_id=schueler.schueler_id,
    datum=date.today()
)
session.add(abwesenheit)
session.commit()

session.close()
print("✅ Dummy-Daten eingefügt")