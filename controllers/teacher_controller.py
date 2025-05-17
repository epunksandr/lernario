from flask import request, redirect, url_for, flash, session

from controllers.class_controller import klassen_service
from services.lehrer_service import LehrerService

ls = LehrerService()


def einloggen():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash("E-Mail und Passwort erforderlich", "danger")
        return redirect(url_for('show_login_form'))

    lehrer_id = ls.login_user(email, password )

    if lehrer_id != 0:
        session['current_teacher_id'] = lehrer_id
        return redirect(url_for('homepage'))
    else:
        flash("Login fehlgeschlagen", "danger")
        return redirect(url_for('show_login_form'))

def register():
    vorname = request.form.get('vorname')
    nachname = request.form.get('nachname')
    email = request.form.get('email')
    password = request.form.get('password')

    if not vorname or not nachname or not email or not password:
        flash("Alle Felder sind erforderlich", "danger")
        return redirect(url_for("show_register"))

    success = ls.register_user(vorname, nachname, email, password)
    if success:
        return redirect(url_for('show_login_form'))
    else:
        flash("Registrierung fehlgeschlagen", "danger")
        return redirect(url_for("show_register"))

def gib_vornamen_des_aktuellen_benutzers() -> int:
    aktueller_benutzer = ls.gib_lehrer(session['current_teacher_id'])
    return aktueller_benutzer.vorname