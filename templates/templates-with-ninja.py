from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)

# A simple todos right 
todos = ["clean the room", "finish with the backend", "fix the db bug"]

@app.route('/get-ip')
def get_ip():
    # Get the ip address
    user_ip = request.remote_addr

    # Set the ip inside of a cookie and make a new response
    response = make_response(redirect('/'))
    response.set_cookie('user_ip', user_ip)

    return response



@app.route('/')
def index():
    # Get the ip address from the cookie
    user_ip = request.cookies.get('user_ip')

    contex = {
        'user_ip' : user_ip,
        'todos' : todos
    }
    
    # Rendering htmls, now expand all the variables with "**"
    return render_template('hello.html', url_for = url_for, **contex)

