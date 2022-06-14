from flask import Flask, request, redirect
import unitest


app = Flask(__name__)

@app.cli.command()
def test():
    pass

@app.route('/')
def home():
    return 'hello'
