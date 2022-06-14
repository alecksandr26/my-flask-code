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
