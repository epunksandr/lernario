from flask import Flask, render_template, session

from controllers.custom_blueprint import CustomBlueprint
from controllers.noten_controller import noten_bp
from controllers.teacher_controller import einloggen, register, gib_vornamen_des_aktuellen_benutzers
from controllers.class_controller import klassen_bp
from controllers import class_controller
from controllers.student_controller import schueler_bp
from controllers.termine_controller import termine_bp
from db.tabellen_anlegen import tabellen_anlegen
from services.schueler_service import SchuelerService
from services.klassen_service import KlassenService
schueler_service = SchuelerService()
klassen_service = KlassenService()

from datetime import date
from babel.dates import format_date

tabellen_anlegen()
app = Flask(__name__, template_folder="templates")
app.secret_key = 'supergeheim123'

app.register_blueprint(schueler_bp, url_prefix="/schueler")
app.register_blueprint(klassen_bp)
app.register_blueprint(termine_bp)
app.register_blueprint(noten_bp)

@app.route('/', methods=['GET'])
def show_register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def handle_register():
    return register()

@app.route('/login', methods=['GET'])
def show_login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    return einloggen()

@app.route('/homepage')
def homepage():
    cur_lehrer_id = session['current_teacher_id']
    vorname_des_benutzers = gib_vornamen_des_aktuellen_benutzers()
    schueleranzahl = schueler_service.gib_schueleranzahl_von_lehrer(cur_lehrer_id)
    klassenanzahl = klassen_service.gib_klassenanzahl(cur_lehrer_id)
    schueler_mit_fehlzeiten_in_dieser_woche = schueler_service.gib_abwesenheiten_von_dieser_woche()
    datum = date.today()
    formatiertes_datum = format_date(datum, "eeee, d. MMMM", "de")
    return render_template('homepage.html',
                           datum=formatiertes_datum,
                           vorname_des_benutzers=vorname_des_benutzers,
                           klassenanzahl=klassenanzahl,
                           schueleranzahl=schueleranzahl,
                           schueler_mit_fehlzeiten_in_dieser_woche=schueler_mit_fehlzeiten_in_dieser_woche,
                           active_page="homepage")


if __name__ == '__main__':
    app.run(debug=True)