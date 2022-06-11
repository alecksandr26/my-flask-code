# To manage erros like 404 page not found
Its important that every page that we created have an error manage for those cases that someone sends to our server bad querys or bad requests, to learn how to deal with those cases I create a .py file like this.
```
from flask import Flask, request, render_template



app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello'



@app.route('/')
def index():
    return render_template('home.html')

```
