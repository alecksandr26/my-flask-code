from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)

@app.route('/get-ip')
def get_ip():
    # Get the ip address
    user_ip = request.remote_addr

    # Set the ip inside of a cookie making a response
    response = make_response(redirect('/'))
    response.set_cookie('user_ip', user_ip)

    return response



@app.route('/')
def index():
    # Get the ip address from the cookie
    user_ip = request.cookies.get('user_ip')
    
    # Rendering htmls
    return render_template('hello.html', user_ip = user_ip, url_for = url_for)

