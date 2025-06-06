from flask import request, redirect, url_for, flash, session

from controllers.klassen_controller import klassen_service
from services.lehrer_service import LehrerService

lehrer_service = LehrerService()

def einloggen():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return redirect(url_for('show_login_form'))

    lehrer_id = lehrer_service.login_user(email, password )

    if lehrer_id != 0:
        session['current_teacher_id'] = lehrer_id
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('show_login_form'))

def register():
    vorname = request.form.get('vorname')
    nachname = request.form.get('nachname')
    email = request.form.get('email')
    password = request.form.get('password')

    if not vorname or not nachname or not email or not password:
        return redirect(url_for("show_register"))

    success = lehrer_service.register_user(vorname, nachname, email, password)
    if success:
        return redirect(url_for('show_login_form'))
    elif success == "FASLE":
        return redirect(url_for("show_login_form"))
    else:
        return redirect(url_for("show_register"))