from flask import request, redirect, url_for, flash, session
from services.teacher_service import login_user, gib_lehrer, register_user


def einloggen():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash("E-Mail und Passwort erforderlich", "danger")
        return redirect(url_for('show_login_form'))

    auth_result = login_user(email, password)

    if auth_result:
        session['current_teacher_id'] = auth_result['lehrer_id']
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

    success = register_user(vorname, nachname, email, password)
    if success:
        return redirect(url_for('show_login_form'))
    else:
        flash("Registrierung fehlgeschlagen", "danger")
        return redirect(url_for("show_register"))

def gib_vornamen_des_aktuellen_benutzers() -> int:
    aktueller_benutzer = gib_lehrer(session['current_teacher_id'])
    return aktueller_benutzer[0]['vorname']