from flask import Blueprint, render_template, session, request, redirect, url_for, flash

from controllers.base.termine_base_blueprints import TermineBlueprint
from controllers.klassen_controller import klassen_service
from services.termine_service import TermineService
from services.klassen_service import KlassenService
from datetime import datetime

termine_bp = TermineBlueprint("termine", "termine")


termine_service = TermineService()
klassen_service = KlassenService()

@termine_bp.route('/')
def uebersicht():
    termine_liste = termine_service.gib_alle_termine_von_lehrer(session['current_teacher_id'])
    klassen_liste = klassen_service.gib_alle_klassen_von_lehrer(session['current_teacher_id'])
    return render_template('termine.html', termine_liste=termine_liste, klassen_liste=klassen_liste, active_page="kalender")

@termine_bp.route('/anzeigen/<int:termin_id>')
def anzeigen(termin_id):
    pass