from flask import render_template, session

from controllers.base.klassen_base_blueprints import KlassenBlueprint
from services.klassen_service import KlassenService

klassen_bp = KlassenBlueprint("klassen", __name__)

klassen_service = KlassenService()

@klassen_bp.route('/')
def uebersicht():
    # Alle Klassen mit der Anzahl der Schüler abrufen
    klassen_liste = klassen_service.gib_klassen_mit_schueleranzahl_von_lehrer(session['current_teacher_id'])
    return render_template('klassenverwaltung.html', klassen_liste=klassen_liste, active_page="klassen")

@klassen_bp.route('/anzeigen/<int:klasse_id>')
def anzeigen(klasse_id):
    klasse = klassen_service.gib_klasse(klasse_id)
    schueler_anzahl = klassen_service.gib_schueleranzahl_von_klasse(session['current_teacher_id'])
    return render_template('klasseninfo.html', schueler_anzahl=schueler_anzahl, klasse=klasse)