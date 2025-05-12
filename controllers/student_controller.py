from flask import Blueprint, jsonify, render_template
from services import schueler_service

schueler_bp = Blueprint('schueler', __name__, url_prefix="/schueler")

@schueler_bp.route('/', methods=['GET'])
def uebersicht():
    schueler_liste = schueler_service.gib_alle_schueler_mit_grundinformationen()
    return render_template("schueler.html", schueler_liste=schueler_liste, active_page="schueler")

@schueler_bp.route('/<int:id>/loeschen')
def loeschen(id):
    schueler_service.loesche_schueler(id)