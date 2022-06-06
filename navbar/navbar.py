
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

