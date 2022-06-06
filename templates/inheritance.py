"""
This is an exmple of how can do inheritance with the templates
"""


from flask import Flask, render_template, request

app = Flask(__name__)


todos = ["Clean my room", "Write the subroutine", "Fix the bug"]


@app.route('/')
def root():
    
    # I pass the todos
    return render_template("content.html", todos = todos, title = "Root")

