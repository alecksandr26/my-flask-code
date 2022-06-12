from flask import Flask, render_template

# Here I import the module bootstrap
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# Here with this we give access to our files 
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('home.html')
