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
Like this this is how we can include the base bootstrap file, you are going to notice that bootstrap is installed when you see this type of letters.
![image](https://user-images.githubusercontent.com/66882463/173209706-e10de857-c8fc-49d7-9610-9478a3353703.png)<br />
So lets see we can import some components of bootstrap so this is the link of the components. <br />
[components](https://getbootstrap.com/docs/3.3/components/)<br />
So for example I'm going to copy this component and paste inside of my html file.
```
{% extends 'bootstrap/base.html' %}

{% block head %}
{{ super() }}
<title>Bootstrap extesion</title>

{% endblock %}

{% block body %}
<ul class="nav nav-pills">
  <li role="presentation" class="active"><a href="#">Home</a></li>
  <li role="presentation"><a href="#">Profile</a></li>
  <li role="presentation"><a href="#">Messages</a></li>
</ul>
<p>Testing the bootstrap</p>


{% endblock %}
```
