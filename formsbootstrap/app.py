"""
We are going to create a simple login 
"""

from flask import Flask, request, make_response, session, redirect, render_template

app = Flask(__name__)

app.config["SECRET_KEY"] = 'mykey'


@app.route('/')
def index():
    return 'hello'
