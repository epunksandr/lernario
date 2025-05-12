from flask import request, redirect, url_for, flash
from services import student_service

def add_new_student():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    klasse = request.form.get('klasse')

    if not fname or lname or klasse:
        flash("es fehlen daten", "danger")
        return redirect(url_for('/schueler/hinzufuegen'))

    success = class_service.add_class(klassenname)

    if success:
        return redirect(url_for('klassen'))
    else:
        flash("Hinzufügen fehlgeschlagen", "danger")
