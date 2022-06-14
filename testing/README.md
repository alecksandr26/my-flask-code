# Testing in flask
Its important to test our code all the time to make sure that our page is working and its important when we are adding new functions to our web or project.<br />
lets start firstly we need to install another module called `flask-testing`, just run this command.
```
$ pip install flask-testing
```
Now with this we cam import a python library called `unitest` and as we create this error routes we can add another route to execute all the tests that we integrate to our app just like this.
```
from flask import Flask, request, redirect
import unittest


app = Flask(__name__)

@app.cli.command()
def test():
    pass

@app.route('/')
def home():
    return 'hello'
```
So inside of this function test we are going to put all our unittest of our code, then we need to create another directory called tests where we are going to store all the tests this is necessary.
```
from flask import Flask, request, redirect
import unittest

app = Flask(__name__)

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.route('/')
def home():
    return 'hello'
```
With this we can run this commmand and this command is going to run all the tests.
```
$ flask test
```
![image](https://user-images.githubusercontent.com/66882463/173676393-811f0680-12d9-4212-9191-513d52af7b3b.png)<br />
Now inside of this new folder called `tests` we are going to create a new file '.py' called `test_base.py` which is going to be a test, inside of this file we are going to import `TestCase` from `flask_testing` to create a test case class where we should add the tests.
```
from flask_testing import TestCase
from flask import current_app
from app import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(curren_app)
```
To add a test as you can see we only need to put a function with his name stats with `test`, now If I run all the tests somthing like this should apears.<br />
![image](https://user-images.githubusercontent.com/66882463/173678337-c2835e18-7776-45af-90b8-1c8871f2c736.png)<br />
Lets test a little bit more, for exmaple I modify our app to make a redirect.
```
from flask import Flask, request, redirect, session, make_response
import unittest


app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.route('/hello')
def hello():
    if session.get('user_ip'):
        return f"hello {session.get('user_ip')}"
    return f"We need an ip"
    

@app.route('/')
def home():
    user_ip = request.remote_addr
    session['user_ip'] = user_ip
    response = make_response(redirect('/hello'))
    return response
```
So yeah we can create a lot of tests you should watch and read the documentation.
