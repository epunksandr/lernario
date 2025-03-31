from flask import Flask
from controllers.user_controller import user_bp

app = Flask(__name__)
    
app.register_blueprint(user_bp, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True)