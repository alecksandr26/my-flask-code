# Dealing with forms
To deal with forms in flask there is an extesion that we should use called `flask wtf`, to install this extesion just run.
```
$ pip install flask-wtf
```
Now we are ready to work with that extesion, we just include `FlaskForm` to work with forms, and to play with this module, we only need to create a new class inherited from `FlaskForm` like this.
```
"""
We are going to create a simple login 
"""

from flask import Flask, request, make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)
bootstrap  = Bootstrap(app)

app.config["SECRET_KEY"] = 'mykey'


@app.route('/')
def index():
    return 'hello'
```

