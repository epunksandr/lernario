from flask import Blueprint, jsonify, render_template, flash, redirect, url_for, request
from services import schueler_service, class_service

schueler_bp = Blueprint('schueler', __name__, url_prefix="/schueler")

@schueler_bp.route('/', methods=['GET'])
def uebersicht():
    schueler_liste = schueler_service.gib_alle_schueler_mit_grundinformationen()
    return render_template("schueler.html", schueler_liste=schueler_liste, active_page="schueler")

@schueler_bp.route('/erstellen', methods=['GET', 'POST'])
def erstellen():
    #POST
    if request.method == 'POST':
        pass
    #GET
    klassen = class_service.get_all_classnames()
    return render_template('schueler_hinzufuegen.html', klassen=klassen)

@schueler_bp.route('/anzeigen/<int:schueler_id>')
def anzeigen(schueler_id):
    pass

@schueler_bp.route('/aktualisieren/<int:schueler_id>')
def aktualisieren(schueler_id):
    pass

@schueler_bp.route('/loeschen/<int:schueler_id>')
def loeschen(schueler_id):
    schueler_service.loesche_schueler(schueler_id)
    return redirect(url_for('schueler.uebersicht'))
