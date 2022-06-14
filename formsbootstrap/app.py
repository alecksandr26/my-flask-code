"""
We are going to create a simple login 
"""

from flask import Flask, request, make_response, session, redirect, render_template, url_for
from flask_bootstrap import Bootstrap

# import the flask class
from flask_wtf import FlaskForm
# The reference functions
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap  = Bootstrap(app)

app.config["SECRET_KEY"] = 'mykey'

class LoginForm(FlaskForm):
    username = StringField("User name: ", validators = [DataRequired()])
    password = PasswordField("User password", validators = [DataRequired()])
    submit = SubmitField('Send')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # I create a contex to pass all the argumetns
    contex = {
        'url_for' : url_for,
        'login_form' : LoginForm() # Creates an instance
    }

    if request.method == "POST" or contex['login_form'].validate_on_submit():
        # Get the data
        username = contex['login_form'].username.data
        password = contex['login_form'].password.data
        session['user'] = { 'username' : username, 'password' : password }
        return redirect('/')

    return render_template('login.html', **contex)


@app.route('/', methods = ['GET'])
def home():
    if not session.get('user'):
        return  redirect('/login')

    contex = {
        'user' : session.get('user')
    }
    
    return render_template('home.html', **contex)
