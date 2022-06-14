from flask import Flask, request, session, make_response, redirect


app = Flask(__name__)

# To have a secret key
app.config['SECRET_KEY'] = 'mykey'

@app.route('/hello')
def hello():
    # Try to fecth the data
    if not session.get('user_ip'):
        return 'We need an ip'
    
    return f"Hello {session.get('user_ip')}"
    

@app.route('/')
def index():
    response = make_response(redirect('/hello'))
    
    # Store my value 
    session['user_ip'] = request.remote_addr

    return response



