from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def root():
    # Get the ip address
    user_ip = request.remote_addr
    
    # Rendering htmls
    return render_template('hello.html', user_ip = user_ip)

