from flask import Flask, render_template
from controllers.user_controller import einloggen

app = Flask(__name__)
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
    return render_template('homepage.html')
    

if __name__ == '__main__':
    app.run(debug=True)