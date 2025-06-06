from flask import Flask, render_template, session

from controllers.lehrer_controller import einloggen, register, lehrer_service
from controllers.klassen_controller import klassen_bp
from controllers.schueler_controller import schueler_bp
from controllers.termine_controller import termine_bp
from db.tabellen_anlegen import tabellen_anlegen
from services.schueler_service import SchuelerService
from services.klassen_service import KlassenService
from services.termine_service import TermineService
from services.lehrer_service import LehrerService
schueler_service = SchuelerService()
klassen_service = KlassenService()
termin_service = TermineService()
lehrer_service = LehrerService()

from datetime import date
from babel.dates import format_date

tabellen_anlegen()
app = Flask(__name__, template_folder="templates")
app.secret_key = 'supergeheim123'

app.register_blueprint(schueler_bp, url_prefix="/schueler")
app.register_blueprint(klassen_bp, url_prefix="/klassen")
app.register_blueprint(termine_bp, url_prefix="/termine")

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
    vorname_des_benutzers = lehrer_service.gib_lehrer(cur_lehrer_id).vorname
    schueleranzahl = schueler_service.gib_schueleranzahl_von_lehrer(cur_lehrer_id)
    klassenanzahl = klassen_service.gib_klassenanzahl(cur_lehrer_id)
    datum = date.today()
    formatiertes_datum = format_date(datum, "eeee, d. MMMM", "de")
    termine_liste = termin_service.gib_alle_termine_von_lehrer(cur_lehrer_id, 3)
    if termine_liste:
        naechster_termin = termine_liste[0]
    else:
        naechster_termin = None

    return render_template('homepage.html',
                           datum=formatiertes_datum,
                           vorname_des_benutzers=vorname_des_benutzers,
                           klassenanzahl=klassenanzahl,
                           schueleranzahl=schueleranzahl,
                           naechster_termin=naechster_termin,
                           termine_liste=termine_liste,
                           active_page="homepage")


if __name__ == '__main__':
    app.run(debug=True, port=8000)