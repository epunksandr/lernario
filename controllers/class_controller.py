from flask import request, redirect, url_for, flash, Blueprint, render_template
from services import class_service

klassen_bp = Blueprint('klassen', __name__, url_prefix="/klassen")

@klassen_bp.route('/', methods=['GET'])
def uebersicht():
    klassen_liste = class_service.get_all_classes_with_students_count()
    return render_template('klassenverwaltung.html', klassen_liste=klassen_liste, active_page="klassen")

@klassen_bp.route('/hinzufuegen', methods=['POST'])
def hinzufuegen():
    klassenname = request.form.get('klassenname')

    flash("klassenname erforderlich", "danger")

    if not klassenname:
        flash("klassenname erforderlich", "danger")
        return redirect(url_for('klassen.uebersicht'))

    class_service.add_class(klassenname)
    return redirect(url_for('klassen.uebersicht'))

@klassen_bp.route('/<int:klasse_id>/loeschen')
def loeschen(klasse_id):
    class_service.delete_class(klasse_id)
    return redirect(url_for('klassen.uebersicht'))

@klassen_bp.route('/bearbeiten/<int:klasse_id>')
def bearbeiten(klasse_id):
    pass

def get_all_classnames():
    return class_service.get_all_classnames()
