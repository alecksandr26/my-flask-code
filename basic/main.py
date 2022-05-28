"""
To run this app we need to declare a variable in to the shell
In linux we run the command export.

"export FLASK_APP=main.py"

After run this another command

"flask run"

"""
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



