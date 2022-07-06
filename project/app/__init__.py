"""
This is the app of todo list in python flask
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .config import Config

# Import the blueprint
from .auth import auth

# Import the user model class
from .models import UserModel


# To create a login manager
login_manager = LoginManager()

# Define the where is the view to create a token when it is logged
login_manager.login_view = 'auth.login'

# Pass the function that login_manager will use to log a user
@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)
    

# create_app: Just creates the app and return it 
def create_app():
    app = Flask(__name__)
    
    # Load the configuration from the object config
    app.config.from_object(Config)
    bootstrap = Bootstrap(app)

    # Initialize the login manager
    login_manager.init_app(app)
    
    # Add the blueprints that we have
    app.register_blueprint(auth)
    return app
    


