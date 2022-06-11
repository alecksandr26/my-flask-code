from flask import Flask, request, render_template



app = Flask(__name__)



# Just like this we can deal with the different type of errors
@app.errorhandler(404)
def error_404(error):
    return render_template('pagenotfound.html')


@app.route('/hello')
def hello():
    return 'Hello'


@app.route('/')
def index():
    return render_template('home.html')
