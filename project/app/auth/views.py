
"""
Import the auth Blueprint
"""

from . import auth
from app.forms import LoginForm
from flask import render_template, url_for, request, session, redirect, flash
from app.firestore_service import get_user_by_id

# Import from models the userdata
from app.models import UserData, UserModel

# Import the method to finish the login of the user
from flask_login import login_user


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
            if password_from_db == login_form.password.data:
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


