"""
This is the main file of the app
"""
# Load the config file
from dotenv import dotenv_values
config = dotenv_values(".env")

import os
# To connect to the gcloud wihtout problesm we need to have this enviorment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config['KEY_JSON']

# Import the app factory
from app import create_app

# Import the forms
from app.forms import LoginForm

from flask import render_template, session, url_for, redirect

# For Testing purpuse
import unittest

# Import the firestore_services
from app.firestore_service import get_users, get_todos_from_user

# To make sure that the user is logged
from flask_login import login_required, current_user

# Creates the app flask
app = create_app()

# The rotue for testing
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.route('/', methods = ['GET'])
@login_required # Adding this decorator to make sure that we are logged
def home():
    # Create a contex
    contex = {
        'todos' : get_todos_from_user(user_id = current_user.id),
        'username' : current_user.id
    }
    
    return render_template('home.html', **contex)







