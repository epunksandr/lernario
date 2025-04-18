from flask import request, redirect, url_for, flash
from services import class_service

def add_new_class():
    klassenname = request.form.get('klassenname')

    if not klassenname:
        flash("klassenname erforderlich", "danger")
        return redirect(url_for('klassenverwaltung'))

    success = class_service.add_class(klassenname)

    if success:
        return redirect(url_for('klassenverwaltung'))
    else:
        flash("Hinzufügen fehlgeschlagen", "danger")

def get_all_classes_with_students_count():
    return class_service.get_all_classes_with_students_count()

def loeschen(class_id):
    class_service.delete_class(class_id)
    return redirect(url_for('klassenverwaltung'))
