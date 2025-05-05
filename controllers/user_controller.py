from flask import request, redirect, url_for, flash, session
from services.authentification_service import login_user



def einloggen():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash("E-Mail und Passwort erforderlich", "danger")
        return redirect(url_for('show_login_form'))

    auth_result = login_user(email, password)

    if auth_result:
        session['user_email'] = auth_result['email'] 
        return redirect(url_for('homepage'))
    else:
        flash("Login fehlgeschlagen", "danger")
        return redirect(url_for('show_login_form'))
