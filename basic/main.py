"""
To run this app we need to declare a variable in to the shell
In linux we run the command export.

"export FLASK_APP=main.py"

After run this another command

"flask run"

"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello my mennnn....'



