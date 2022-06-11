from flask import Flask, request, render_template



app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello'



@app.route('/')
def index():
    return render_template('home.html')
