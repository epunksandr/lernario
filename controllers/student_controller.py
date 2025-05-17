from flask import Blueprint, jsonify, render_template, flash, redirect, url_for, request, session

from controllers.base.schueler_base_blueprints import SchuelerBlueprint
from services.schueler_service import SchuelerService
from services.klassen_service import KlassenService
import inspect

schueler_bp = SchuelerBlueprint("schueler", __name__)



schueler_service = SchuelerService()
class_service = KlassenService()

@schueler_bp.route('/', methods=['GET'])
def uebersicht():
    schueler_liste = schueler_service.gib_alle_schueler_mit_grundinformationen(session['current_teacher_id'])
    print(schueler_liste)
    klassen_liste = class_service.gib_alle_klassen()
    return render_template("schueler.html",
                           schueler_liste=schueler_liste,
                           klassen_liste=klassen_liste,
                           active_page="schueler")

@schueler_bp.route('/anzeigen/<int:schueler_id>')
def anzeigen(schueler_id):
    pass

@schueler_bp.route('/aktualisieren/<int:schueler_id>')
def aktualisieren(schueler_id):
    pass
