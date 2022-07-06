
"""
Import the auth Blueprint
"""

from . import auth
from app.forms import LoginForm, SignUpForm
from flask import render_template, url_for, request, session, redirect, flash
from app.firestore_service import get_user_by_id, user_put

# Import from models the userdata
from app.models import UserData, UserModel

# Import the method to finish the login of the user
from flask_login import login_user, login_required, logout_user

# For password hashing
from werkzeug.security import generate_password_hash, check_password_hash


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
        user_doc = get_user_by_id(login_form.username.data)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']
            if check_password_hash(password_from_db, login_form.password.data):
                user_data = UserData(login_form.username.data, password_from_db)
                user = UserModel(user_data)

                login_user(user) # Make sure that the user is logged
                
                return redirect(url_for('home'))
                
            else:
                contex['error'] = "Password incorrect"
        else:
            contex['error'] = "Error that user doesn't exist"
            
        return render_template('login.html', **contex)
        
        
    return render_template('login.html', **contex)



@auth.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    signup_form = SignUpForm()
    
    contex = {
        'signup_form' : signup_form,
        'url_for' : url_for
    }

    if request.method == "POST":
        user_doc = get_user_by_id(signup_form.username.data)

        if user_doc.to_dict() is None:
            print(signup_form.password.data)
            hash_pass = generate_password_hash(signup_form.password.data)
            user_data = UserData(signup_form.username.data, hash_pass)
            user_put(user_data)
            
            user = UserModel(user_data)
            login_user(user)
            
            return redirect(url_for('home'))
        else:
            contex['error'] = "That username already exist"
    

    return render_template('signup.html', **contex)


