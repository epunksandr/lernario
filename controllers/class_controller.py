from flask import request, redirect, url_for, flash, Blueprint, render_template

from services.klassen_service import KlassenService

klassen_bp = Blueprint('klassen', __name__, url_prefix="/klassen")

klassen_service = KlassenService()

@klassen_bp.route('/')
def uebersicht():
    # Alle Klassen mit der Anzahl der Schüler abrufen
    klassen_liste = klassen_service.get_all_classes_with_students_count()
    print(klassen_liste)  # Debugging-Ausgabe, um sicherzustellen, dass Daten korrekt abgerufen werden
    return render_template('klassenverwaltung.html', klassen_liste=klassen_liste, active_page="klassen")

@klassen_bp.route('/erstellen', methods=['POST'])
def erstellen():
    klassenname = request.form.get('klassenname')

    if not klassenname:
        flash("Klassenname erforderlich", "danger")
        return redirect(url_for('klassen.uebersicht'))

    klassen_service.erstelle_klasse(klassenname)
    flash("Klasse erfolgreich hinzugefügt", "success")
    return redirect(url_for('klassen.uebersicht'))

@klassen_bp.route('/anzeigen/<int:klasse_id>')
def anzeigen(klasse_id):
    klasse = klassen_service.gib_klasse(klasse_id)
    return render_template('klasseninfo.html', klasse=klasse)

@klassen_bp.route('/aktualisieren/<int:klasse_id>')
def aktualisieren(klasse_id):
    pass

@klassen_bp.route('/<int:klasse_id>/loeschen')
def loeschen(klasse_id):
    klassen_service.loesche_klasse(klasse_id)
    return redirect(url_for('klassen.uebersicht'))

def get_all_classnames():
    return klassen_service.get_all_classnames()
