from flask import Blueprint, jsonify, render_template, flash, redirect, url_for
from services import schueler_service, class_service

schueler_bp = Blueprint('schueler', __name__, url_prefix="/schueler")

@schueler_bp.route('/', methods=['GET'])
def uebersicht():
    schueler_liste = schueler_service.gib_alle_schueler_mit_grundinformationen()
    return render_template("schueler.html", schueler_liste=schueler_liste, active_page="schueler")

@schueler_bp.route('/<int:schueler_id>/loeschen')
def loeschen(schueler_id):
    schueler_service.loesche_schueler(schueler_id)
    return redirect(url_for('schueler.uebersicht'))

@schueler_bp.route('/schueler/hinzufuegen/', methods=['GET'])
def schueler_hinzufuegen_seite():
    klassen = class_service.get_all_classnames()
    print(klassen)
    return render_template('schueler_hinzufuegen.html', klassen=klassen)

@schueler_bp.route('/schueler/hinzufuegen/', methods=['POST'])
def schueler_hinzufuegen():
    return None