from urllib import request

from flask import Flask, render_template
from controllers.user_controller import einloggen
from controllers.class_controller import add_new_class
from controllers.class_controller import get_all_classes_with_students_count
from controllers import class_controller
from controllers.student_controller import schueler_bp

app = Flask(__name__, template_folder="templates")
app.secret_key = 'supergeheim123'

app.register_blueprint(schueler_bp)

@app.route('/', methods=['GET'])
def show_register():
    return render_template('register.html')

@app.route('/login', methods=['GET'])
def show_login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    return einloggen()

@app.route('/homepage')
def homepage():
    return render_template('homepage.html', active_page="homepage")

@app.route('/termin')
def show_termin_form():
    return render_template('termin-form.html')

@app.route('/klassenverwaltung')
def klassen():
    klassen_liste = get_all_classes_with_students_count()

    print(klassen_liste)

    return render_template('klassenverwaltung.html', klassen_liste=klassen_liste)
    
@app.route('/noten')
def noten():
    return render_template('noten.html', active_page="noten")

@app.route('/kalender')
def kalender():
    return render_template('kalender.html', active_page="kalender")

@app.route('/neue_klasse', methods=['POST'])
def neue_klasse():
    return add_new_class()


@app.route('/loeschen/<int:klasse_id>', methods=['GET', 'POST'])
def loeschen(klasse_id):
    return class_controller.loeschen(klasse_id)

@app.route('/bearbeiten/<int:klasse_id>', methods=['GET', 'POST'])
def bearbeiten(klasse_id):
    class_controller.bearbeiten(klasse_id)

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