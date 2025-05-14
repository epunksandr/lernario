from flask import Flask, render_template, session
from controllers.teacher_controller import einloggen, register, gib_vornamen_des_aktuellen_benutzers
from controllers.class_controller import klassen_bp
from controllers import class_controller
from controllers.student_controller import schueler_bp
from controllers.termine_controller import termine_bp
from services import schueler_service, class_service

from datetime import date
from babel.dates import format_date

app = Flask(__name__, template_folder="templates")
app.secret_key = 'supergeheim123'

app.register_blueprint(schueler_bp)
app.register_blueprint(klassen_bp)
app.register_blueprint(termine_bp)

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
    klassenanzahl = class_service.gib_klassenanzahl(cur_lehrer_id)
    schueler_mit_fehlzeiten_in_dieser_woche = schueler_service.gib_abwesenheiten_von_dieser_woche()
    datum = date.today()
    formatiertes_datum = format_date(datum, "eeee, d. MMMM", "de")
    return render_template('homepage.html',
                           datum=formatiertes_datum,
                           vorname_des_benutzers=vorname_des_benutzers,
                           klassenanzahl=klassenanzahl,
                           schueler_mit_fehlzeiten_in_dieser_woche=schueler_mit_fehlzeiten_in_dieser_woche,
                           active_page="homepage")

@app.route('/noten')
def noten():
    return render_template('noten.html', active_page="noten")

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