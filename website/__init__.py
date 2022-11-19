from flask import Flask
from hidden_details import Details

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Details.flask_secret_key()
    return app