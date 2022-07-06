"""
This file will contain all the forms
"""

# Import the flask form
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


# Create the login object form
class LoginForm(FlaskForm):
    username = StringField("User name", validators=[DataRequired()])
    password = PasswordField("User password", validators=[DataRequired()])
    submit = SubmitField('Send')




class SignUpForm(LoginForm):
    pass



class TodoForm(FlaskForm):
    description = StringField("Description", validators=[DataRequired()])
    submit = SubmitField('Create')


class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Finish')

