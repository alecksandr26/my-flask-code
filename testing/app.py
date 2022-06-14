from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'
