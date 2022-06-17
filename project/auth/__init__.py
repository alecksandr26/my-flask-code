"""
This thing is going to be a Blueprint 
"""
from flask import Blueprint

"""
All the routes with the prefix /auth are going to be redirected to this module
So we are going to create antoher file called views which is going to have all the routes releated
to /auth
"""

auth = Blueprint('auth', __name__, url_prefix='/auth')


"""
Import all the routes
"""

from . import views


