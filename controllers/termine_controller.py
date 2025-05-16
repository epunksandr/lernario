from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from services import termine_service, klassen_service

termine_bp = Blueprint('termine', __name__, url_prefix="/termine")

@termine_bp.route('/')
def uebersicht():
    termine_liste = termine_service.gib_alle_termine()
    return render_template('termine.html', termine_liste=termine_liste, active_page="kalender")

@termine_bp.route('/erstellen')
def erstellen():
    #POST
    if request.method == 'POST':
        termin_name = request.form.get("name")
        klasse_id = request.form.get("klasse")
        datum = request.form.get("datum")

        if not termin_name or not datum:
            flash("Name und Datum des Termins sind erforderlich!", "danger")
            return redirect(url_for("termine.show_termin_form"))

        termine_service.neuer_termin(termin_name, datum, klasse_id)
        return redirect(url_for("termine.uebersicht"))
    #GET
    cur_teacher_id = session['current_teacher_id']
    klassen_liste = class_service.gib_klassen_von_lehrer(cur_teacher_id)
    return render_template('termin-form.html', klassen_liste=klassen_liste)

@termine_bp.route('/anzeigen/<int:termin_id>')
def anzeigen(termin_id):
    pass

@termine_bp.route('/aktualisieren/<int:termin_id>')
def aktualisieren(termin_id):
    pass

@termine_bp.route('/loeschen/<int:termin_id>')
def loeschen(termin_id):
    pass

