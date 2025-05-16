from flask import Blueprint, jsonify, render_template, flash, redirect, url_for, request

from controllers.custom_blueprint import CustomBlueprint
from services import schueler_service, class_service
import inspect

schueler_bp = CustomBlueprint('schueler', 'schueler')

@schueler_bp.route('/', methods=['GET'])
def uebersicht():
    schueler_liste = schueler_service.gib_alle_schueler_mit_grundinformationen()
    klassen_liste = class_service.gib_alle_klassen()
    return render_template("schueler.html",
                           schueler_liste=schueler_liste,
                           klassen_liste=klassen_liste,
                           active_page="schueler")

@schueler_bp.route('/erstellen', methods=['POST'])
def erstellen():
    werte = {}
    method = schueler_service.erstelle_schueler
    sig = inspect.signature(method)
    for name, param in sig.parameters.items():
        werte[name] = request.form.get(name)

    for name, param in sig.parameters.items():
        if param.default != 'None':
            if not werte[name]:
                return redirect(url_for("schueler.uebersicht"))

    method(**werte)
    return redirect(url_for("schueler.uebersicht"))

@schueler_bp.route('/anzeigen/<int:schueler_id>')
def anzeigen(schueler_id):
    pass

@schueler_bp.route('/aktualisieren/<int:schueler_id>')
def aktualisieren(schueler_id):
    pass
