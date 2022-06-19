
"""
Import the auth Blueprint
"""

from . import auth
from app.forms import LoginForm
from flask import render_template, url_for, request, session, redirect, flash
from app.firestore_service import get_users

# This is the route of loggin from the blueprint auth
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    contex = {
        'url_for' : url_for,
        'login_form' : login_form, # Create the instance
        'error' : None
    }
    
    # Create the user and do the request
    if request.method == 'POST':
        # First verify if the user exist
        users = get_users()
        
        for user in users:
            if user.id == login_form.username.data and user.to_dict()['password'] == login_form.password.data:
                session['user'] = {
                    'username' : login_form.username.data,
                    'password' : login_form.password.data
                }
                return redirect(url_for('home'))
        
        contex['error'] = "Error that user doesn't exist"
        return render_template('login.html', **contex)
        
        
    return render_template('login.html', **contex)


