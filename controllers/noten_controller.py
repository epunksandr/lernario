from flask import request, redirect, url_for, flash, Blueprint, render_template

from controllers.base.noten_base_blueprints import NotenBlueprint
from services import klassen_service

noten_bp = NotenBlueprint("noten", __name__)

@noten_bp.route('/')
def uebersicht():
    return render_template('noten.html', active_page="noten")

@noten_bp.route('/anzeigen/<int:note_id>')
def anzeigen(note_id):
    pass

@noten_bp.route('/aktualisieren/<int:note_id>')
def aktualisieren(note_id):
    pass