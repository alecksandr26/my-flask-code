# This is an example of how we can manipulate static files in flask
from flask import Flask, render_template, request

# Here I define the path of the templates and static files
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html")


