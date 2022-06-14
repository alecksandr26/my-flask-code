# Encrypting cookies
Its importnat to matain the data saved, because someone can copie our cookies and if we didn't mantain it saved, someone can use that information on his beneift, so we won't that, we can use some flask functions to mantain that information saved. <br />
The first thing that we need to do is to create our secret key you only need to modify something like this. <br />
```
from flask import Flask


app = Flask(__name__)

# To have a secret key
app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():
    return 'hello'
```
Now We need to include an object called session in from the flask module where we are going to store the data, and its very easy to use it.
```
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
```
Now if you want to get the data you are not going to be able because is encrypted.<br />
![image](https://user-images.githubusercontent.com/66882463/173627158-c966eab4-f995-4c53-9d9f-ec33f91bad93.png)


