from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def showRegister():
    return render_template('register.html')

@app.route('/login')
def showLogin():
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)