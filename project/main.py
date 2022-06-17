"""
This is the main file of the app
"""
# Import the app factory
from app import create_app

# Import the forms
from app.forms import LoginForm

from flask import render_template, session, redirect, url_for


# Creates the app flask
app = create_app()

# This is the route of loggin 
@app.route('/login', methods = ['GET', 'POST'])
def login():
    contex = {
        'url_for' : url_for,
        'login_form' : LoginForm() # Create the instance
    }
    return render_template('login.html', **contex)


@app.route('/')
def home():
    # If there is not user logged redirect to login
    if not session.get('user'): 
        return redirect('login')
    
    return render_template('home.html')


