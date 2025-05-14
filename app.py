from flask import Flask, render_template
from controllers.teacher_controller import einloggen, register, gib_vornamen_des_aktuellen_benutzers
from controllers.class_controller import klassen_bp
from controllers import class_controller
from controllers.student_controller import schueler_bp
from services import termine_service
from services import schueler_service

from datetime import date
from babel.dates import format_date

app = Flask(__name__, template_folder="templates")
app.secret_key = 'supergeheim123'

app.register_blueprint(schueler_bp)
app.register_blueprint(klassen_bp)

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
    vorname_des_benutzers = gib_vornamen_des_aktuellen_benutzers()
    schueler_mit_fehlzeiten_in_dieser_woche = schueler_service.gib_abwesenheiten_von_dieser_woche()
    datum = date.today()
    formatiertes_datum = format_date(datum, "eeee, d. MMMM", "de")
    return render_template('homepage.html',
                           datum=formatiertes_datum,
                           vorname_des_benutzers=vorname_des_benutzers,
                           active_page="homepage")

@app.route('/termin')
def show_termin_form():
    return render_template('termin-form.html')

@app.route('/noten')
def noten():
    return render_template('noten.html', active_page="noten")

@app.route('/termine')
def termine():
    termine_liste = termine_service.gib_alle_termine()
    return render_template('termine.html', termine_liste=termine_liste, active_page="kalender")

@app.route('/schueler/hinzufuegen/', methods=['GET'])
def schueler_hinzufuegen_seite():
    klassen = class_controller.get_all_classnames()
    print(klassen)
    return render_template('schueler_hinzufuegen.html', klassen=klassen)

@app.route('/schueler/hinzufuegen/', methods=['POST'])
def schueler_hinzufuegen():
    return class_controller.add_students()


if __name__ == '__main__':
    app.run(debug=True)