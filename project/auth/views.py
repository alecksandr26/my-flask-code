
"""
Import the auth Blueprint
"""

from . import auth
from app.forms import LoginForm


# This is the route of loggin from the blueprint auth
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    contex = {
        'url_for' : url_for,
        'login_form' : LoginForm() # Create the instance
    }
    
    return render_template('login.html', **contex)


