from flask import request, redirect, url_for, flash, Blueprint, render_template
from services import class_service

noten_bp = Blueprint('noten', __name__, url_prefix="/noten")

@noten_bp.route('/')
def uebersicht():
    return render_template('noten.html', active_page="noten")

@noten_bp.route('/erstellen')
def erstellen():
    pass

@noten_bp.route('/anzeigen/<int:note_id>')
def anzeigen(note_id):
    pass

@noten_bp.route('/aktualisieren/<int:note_id>')
def aktualisieren(note_id):
    pass

@noten_bp.route('/loeschen/<int:note_id>')
def loeschen(note_id):
    pass