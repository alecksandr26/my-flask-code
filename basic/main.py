"""
To run this app we need to declare a variable in to the shell
In linux we run the command export.

"export FLASK_APP=main.py"

After run this another command

"flask run"

"""
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    # Get the ip address
    user_ip = request.remote_addr
    
    return f'Your ip is {user_ip}'



