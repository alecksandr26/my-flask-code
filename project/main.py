"""
This is the main file of the app
"""

from app import create_app
from flask import render_template


# Creates the app flask
app = create_app()

@app.route('/')
def home():
    return render_template('home.html')


