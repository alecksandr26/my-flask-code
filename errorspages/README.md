# To manage erros like 404 page not found
Its important that every page that we created have an error manage for those cases that someone sends to our server bad querys or bad requests, to learn how to deal with those cases I create a `.py` file like this.
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
Where we have two routes right?, `/` and `/hello` And this is the html file `home.html`.
```
<!DOCTYPE html>
<html>
    <head>
        <title>Error pages</title>
    </head>
    <body>
        <p>Simple web page that I created to test the error pages</p>
    </body>
</html>
```
Then flask has a funcion to deal with those cases, the function is `app.errorhandler`, and it receives the type of error which we want to deal, like this, another thing if you take look is that we receives the error msg though the function.
```
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
```
Now the html `pagenotfound.html` is this.
```
<!DOCTYPE html>
<html>
    <head>
        <title>ERROR 404</title>
    </head>
    <body>
        <p>Error that page doesn't exist</p>
    </body>
</html>
```
With this we can render a lot of errors that our server maybe could have in some bad requests.
