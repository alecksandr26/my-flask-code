

"""
This is the app of todo list in python flask
Created by alecksandr26
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config


# create_app: Just creates the app and return it 
def create_app():
    app = Flask(__name__)
    
    # Load the configuration from the object config
    app.config.from_object(Config)
    bootstrap = Bootstrap(app)
    return app
    


