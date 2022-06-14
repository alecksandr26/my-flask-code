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
    return make_response(redirect('/hello'))
