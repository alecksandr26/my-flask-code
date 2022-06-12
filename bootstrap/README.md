# Bootstrap extension
We can work with some extesions of flask, one of favorites is bootstrap, so to install this extresion run this command.
```
pip install flask-bootstrap
```
Now to initlize the bootstrap module is easy we only need to import this function and run it like this.
```
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('home.html')
```
With this now we can load the basic modules of bootstrap inside of our base html, how ?, too easy we only need to import the boostrap base html like this.
```
{% extends 'bootstrap/base.html' %}

{% block head %}
{{ super() }}
<title>Bootstrap extesion</title>

{% endblock %}

{% block body %}

<p>Testing the bootstrap</p>

{% endblock %}

```
