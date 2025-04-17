from flask import Flask, render_template
from controllers.user_controller import einloggen
from controllers.class_controller import add_new_class
from controllers.class_controller import get_all_classes_with_students_count
from controllers import class_controller

app = Flask(__name__, template_folder="templates")
app.secret_key = 'supergeheim123' 

@app.route('/')
def showRegister():
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

@app.route('/klassenverwaltung')
def klassen():
    klassen_liste = get_all_classes_with_students_count()

    print(klassen_liste)

    return render_template('klassenverwaltung.html', klassen_liste=klassen_liste, active_page="klassen")

@app.route('/schueler')
def schueler():
    schueler_liste = [
    {"id": 1, "vorname": "Anna", "nachname": "Müller", "klasse": "10A", "notenschnitt": 2.3, "abwesenheiten": 3},
    {"id": 2, "vorname": "Lukas", "nachname": "Schmidt", "klasse": "10A", "notenschnitt": 1.8, "abwesenheiten": 1},
    {"id": 3, "vorname": "Mia", "nachname": "Lehmann", "klasse": "10A", "notenschnitt": 2.7, "abwesenheiten": 5},
    {"id": 4, "vorname": "Ben", "nachname": "Weber", "klasse": "10A", "notenschnitt": 1.5, "abwesenheiten": 0},
    {"id": 5, "vorname": "Leonie", "nachname": "Koch", "klasse": "10A", "notenschnitt": 2.0, "abwesenheiten": 2},
    {"id": 6, "vorname": "Paul", "nachname": "Richter", "klasse": "10A", "notenschnitt": 3.1, "abwesenheiten": 4},
    {"id": 7, "vorname": "Sophie", "nachname": "Hoffmann", "klasse": "10A", "notenschnitt": 1.9, "abwesenheiten": 0},
    {"id": 8, "vorname": "Tim", "nachname": "Fischer", "klasse": "10A", "notenschnitt": 2.4, "abwesenheiten": 3},
    {"id": 9, "vorname": "Laura", "nachname": "Wagner", "klasse": "10A", "notenschnitt": 2.6, "abwesenheiten": 2},
    {"id": 10, "vorname": "Jonas", "nachname": "Schneider", "klasse": "10A", "notenschnitt": 1.7, "abwesenheiten": 1},
]
    return render_template("schueler.html", schueler_liste=schueler_liste, active_page="schueler")
    
@app.route('/noten')
def noten():
    return render_template('noten.html', active_page="noten")

@app.route('/kalender')
def kalender():
    return render_template('kalender.html', active_page="kalender")

@app.route('/neue_klasse', methods=['POST'])
def neue_klasse():
    return add_new_class()


#@app.route('/loeschen/<int:klasse_id>', methods=['GET', 'POST'])
#def loeschen(klasse_id):
#    class_controller.loeschen(klasse_id)


if __name__ == '__main__':
    app.run(debug=True)