# Templates and Static files
With flask we can return html files, json data and other things so lets try to do an easy html file, so the first thing that you need to do is in your project directory add an templates folder like me.

`$ mkdir templates`

And inside of our python code we are going to import this function `render_template`, like this.
```
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello'

```
So now instead of just return a simple `'hello'` we are going to create an html file inside of our templates directoy, in my case this is my html file.
```
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <h1>Hello There</h1>
    </body>
</html>
```
Now inside of our python code just change that return and use the function `render_template`.
```
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('hello.html')
```
Now flask render this html files in a special way, because uses something called "jinj2" which is able to render and mix some python code inside of a html thats sounds good no ?, so lets see if we can import the ipv address user inside of the html, firstly we need to add another argument to the `render_template` function, like this.
```
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def root():
    # Get the ip address
    user_ip = request.remote_addr
    
    # Rendering htmls
    return render_template('hello.html', user_ip = user_ip)
```
Inside of our html, we need to use the jinja2 syntax like this, if we want to print some variable we use `{{ my var }}`.
```
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <h1>Hello There, this is your ip {{ user_ip }}</h1>
    </body>
</html>
```
Te result is this.

![alt text](./ip.png)

## Control Structures in Jinja2
As I mention before we can run python code inside of the html with the power of Jinja2, so lets how we can run some python code, firstly I modify the last code and I added a new route and also I use some functions.
```
from flask import Flask, render_template, request, make_response, redirect


app = Flask(__name__)

@app.route('/get-ip')
def get_ip():
    # Get the ip address
    user_ip = request.remote_addr

    # Set the ip inside of a cookie making a response
    response = make_response(redirect('/'))
    response.set_cookie('user_ip', user_ip)

    return response



@app.route('/')
def index():
    # Get the ip address from the cookie
    user_ip = request.cookies.get('user_ip')
    
    # Rendering htmls
    return render_template('hello.html', user_ip = user_ip)
```
Now for example if we try to do the `/` will try to get the ip address from a cookie, but if we doens't have that cookie we are going to get a `None` value, to deal with that cases we can add some python code to our html to avoid some errors just like this.
```
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        {% if user_ip %}
        <h1>Hello There, this is your ip {{ user_ip }}</h1>
        {% else %}
        <a href="{{ url_for('get_ip') }}">Get your ip</a>
        {% endif %}
    </body>
</html>


```
An important thing here is the `url_for` function because is a function that flask has that we can use to redirect the user if he press on that link tag, so lets pass that function as argument inside of `render_template` function, like this, another important thing we need to pass the name of the route `url_for('function_name)`.
```
from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)

@app.route('/get-ip')
def get_ip():
    # Get the ip address
    user_ip = request.remote_addr

    # Set the ip inside of a cookie making a response
    response = make_response(redirect('/'))
    response.set_cookie('user_ip', user_ip) 

    return response



@app.route('/')
def index():
    # Get the ip address from the cookie
    user_ip = request.cookies.get('user_ip')
    
    # Rendering htmls
    return render_template('hello.html', user_ip = user_ip, url_for = url_for)
```
Now lets see how we can iterate a smple list I create inside of the code a simple todo list and we can create a dictionary to encapsulate some values.
```
from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)

# A simple todos right 
todos = ["clean the room", "finish with the backend", "fix the db bug"]

@app.route('/get-ip')
def get_ip():
    # Get the ip address
    user_ip = request.remote_addr

    # Set the ip inside of a cookie and make a new response
    response = make_response(redirect('/'))
    response.set_cookie('user_ip', user_ip)

    return response



@app.route('/')
def index():
    # Get the ip address from the cookie
    user_ip = request.cookies.get('user_ip')

    contex = {
        'user_ip' : user_ip,
        'todos' : todos
    }
    
    # Rendering htmls, now expand all the variables with "**"
    return render_template('hello.html', url_for = url_for, **contex)
```
An interesting thing here are the double `**` with this we can export all the fields from the contex in a way to avoid to fetch the data insdie of the dictionary.



