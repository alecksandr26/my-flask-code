"""
This is the main file of the app
"""
# Import the app factory
from app import create_app

# Import the forms
from app.forms import LoginForm

from flask import render_template, session, redirect, url_for

# For Testing purpuse
import unittest


# Creates the app flask
app = create_app()

# The rotue for testing
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.route('/')
def home():
    # If there is not user logged redirect to login
    if not session.get('user'): 
        return redirect('login')
    
    return render_template('home.html')


