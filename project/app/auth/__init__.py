"""
Here creates the blue print auth
"""

from flask import Blueprint

"""
The collection of routes releated with auth
"""
auth = Blueprint('auth', __name__, url_prefix = '/auth')


from . import views
