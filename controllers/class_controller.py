from flask import request, redirect, url_for, flash, Blueprint, render_template
from services import class_service

klassen_bp = Blueprint('klassen', __name__, url_prefix="/klassen")

@klassen_bp.route('/', methods=['GET'])
def uebersicht():
    # Alle Klassen mit der Anzahl der Schüler abrufen
    klassen_liste = class_service.get_all_classes_with_students_count()
    print(klassen_liste)  # Debugging-Ausgabe, um sicherzustellen, dass Daten korrekt abgerufen werden
    return render_template('klassenverwaltung.html', klassen_liste=klassen_liste, active_page="klassen")

@klassen_bp.route('/hinzufuegen', methods=['POST'])
def hinzufuegen():
    klassenname = request.form.get('klassenname')

    if not klassenname:
        flash("Klassenname erforderlich", "danger")
        return redirect(url_for('klassen.uebersicht'))

    class_service.add_class(klassenname)
    flash("Klasse erfolgreich hinzugefügt", "success")
    return redirect(url_for('klassen.uebersicht'))

@klassen_bp.route('/<int:klasse_id>/loeschen')
def loeschen(klasse_id):
    class_service.delete_class(klasse_id)
    return redirect(url_for('klassen.uebersicht'))

@klassen_bp.route('/info/<int:klasse_id>')
def info(klasse_id):
    return render_template('klasseninfo.html')

@klassen_bp.route('/bearbeiten/<int:klasse_id>')
def bearbeiten(klasse_id):
    pass

def get_all_classnames():
    return class_service.get_all_classnames()
