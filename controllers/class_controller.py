from flask import request, redirect, url_for, flash, Blueprint, render_template, session

from controllers.base.klassen_base_blueprints import KlassenBlueprint
from services.klassen_service import KlassenService

klassen_bp = KlassenBlueprint("klassen", __name__)

klassen_service = KlassenService()

@klassen_bp.route('/')
def uebersicht():
    # Alle Klassen mit der Anzahl der Schüler abrufen
    klassen_liste = klassen_service.get_all_classes_with_students_count()
    print(klassen_liste)  # Debugging-Ausgabe, um sicherzustellen, dass Daten korrekt abgerufen werden
    return render_template('klassenverwaltung.html', klassen_liste=klassen_liste, active_page="klassen")

@klassen_bp.route('/anzeigen/<int:klasse_id>')
def anzeigen(klasse_id):
    return render_template('klasseninfo.html')

@klassen_bp.route('/aktualisieren/<int:klasse_id>')
def aktualisieren(klasse_id):
    pass

def get_all_classnames():
    return klassen_service.get_all_classnames()
