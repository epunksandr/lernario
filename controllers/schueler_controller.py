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
    cur_lehrer_id = session['current_teacher_id']
    schueler_liste = schueler_service.gib_alle_schueler_mit_grundinformationen(cur_lehrer_id)
    print(schueler_liste)
    klassen_liste = class_service.gib_klassen_von_lehrer(cur_lehrer_id)
    return render_template("schueler.html",
                           schueler_liste=schueler_liste,
                           klassen_liste=klassen_liste,
                           active_page="schueler")

@schueler_bp.route('/anzeigen/<int:schueler_id>')
def anzeigen(schueler_id):
    schueler = schueler_service.gib_schueler(schueler_id)
    return render_template('schuelerinfo.html', schueler=schueler)
