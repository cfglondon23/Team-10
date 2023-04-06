from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_mail import Mail, Message

import secrets

# Generate a random byte string of length 32



from werkzeug.security import generate_password_hash, check_password_hash

# creating a database instance
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message_category = "info"


def create_app():
    """Construct the core app object."""
    app = Flask(__name__)

    with app.app_context():
        SECRET_KEY = secrets.token_bytes(32)
        app.config['SECRET_KEY'] = 'SECRET_KEY'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        
        app.config["SECURITY_PASSWORD_SALT"] = 'wjwksmqbfscbnzjgsdj'
        
        db.init_app(app)
        login_manager.init_app(app)
        db.create_all()
     

    return app,mail