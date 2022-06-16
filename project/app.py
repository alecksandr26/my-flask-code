from flask import Flask, request, render_template, url_for, make_response, redirect


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


