# Creating a navbar
To do a navbar inside of our page is too easy to do it, we only need to create our base.html for all the html files inside of our plataform, and for each section we should create another html tfiles, so inside of my python file I create a decorator to catch each function name.
```
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


links = []

def getName(func):
    global links
    links.append(func.__name__)
    return func
    

@app.route('/blog')
@getName
def blog():
    return render_template('blog.html', url_for = url_for, links = links)
    


@app.route('/')
@getName
def root():
    return render_template('navbar.html', url_for = url_for, links = links)
```
This is my base.html also I create a macros function to render each navbar insdie of each page.
```
<!DOCTYPE html>

<html>
    <head>
        <title>NavBar | {% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
</html>
```
And this is my macros.html.
```
{% macro render_nav_bar(links) %}
<nav>
    <ul>
        {% for l in links %}
        <li><a href="{{ url_for(l) }}">{{ l }}</a></li>
        {% endfor %}
    </ul>
</nav>
{% endmacro %}
```
Finaly I just have two sections so These are the files.
```
{% extends 'base.html' %}

{% import 'macros.html' as macros %}


{% block title %}
Blog
{% endblock %}


{% block content %}
{{ macros.render_nav_bar(links) }}
<h3>Blog:</h3>
{% endblock %}
```
```
{% extends 'base.html' %}

{% import 'macros.html' as macros %}


{% block title %}
Root
{% endblock %}


{% block content %}
{{ macros.render_nav_bar(links) }}
<h3>Root:</h3>
{% endblock %}
```
