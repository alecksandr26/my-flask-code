"""
This file will contain all the forms
"""

# Import the flask form
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField


# Create the login object form
class LoginForm(FlaskForm):
    username = StringField("User name")
    password = PasswordField("User password")
    submit = SubmitField('Send')


