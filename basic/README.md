# To run
It is easy you can create a shell variable called `FLASK_APP` and yout put the name of the file.

`$ export FLASK_APP=main.py`

After that with the flask command we can run the app.

`$ flask run`

## Debugging with flask
To debug with flask, we need to create another shell variable called  `FLASK_DEBUG` and you need to set this variable with "1".

`$ export FLASK_DEBUG=1`

With this variable, we can make a change inside of the file and that change will be automatically applied to the server, also make sure your self that you have set this another the `FLASK_ENV` variable as `development` like this.

`$ export FLASK_ENV=development`

# Request and Response
## Request
To use request we need to import this object, this object will has some variables that we can get information.

```
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    # Get the ip address
    user_ip = request.remote_addr
    
    return f'Your ip is {user_ip}'
```

## Response
We can manipulate the response for example we can redirect the users, for example here if the user try to load the `/` root path will be redirect to the `/ip`, another important thing we can catch and save the ip address in the `/` route.
```
from flask import Flask, request, make_response, redirect


app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    
    # make a resopnse and fetch data from the '/hello'
    response = make_response(redirect('/ip'))

    # Create a cookie to save the user_ip
    response.set_cookie('user_ip', user_ip)

    return response
    

# So we end here
@app.route('/ip')
def hello():
    # Get the ip address from the cooki that we just created
    user_ip = request.cookies.get('user_ip')
    
    return f'Your ip is {user_ip}'
```
