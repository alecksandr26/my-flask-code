# Templates and Static files
With flask we can return html files, json data and other things so lets try to do an easy html file, so the first thing that you need to do is in your project directory add an templates folder like me.

`$ mkdir templates`

And inside of our python code we are going to import this function `render_template`, like this.
```
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello'

```
So now instead of just return a simple `'hello'` we are going to create an html file inside of our templates directoy, in my case this is my html file.
```
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <h1>Hello There</h1>
    </body>
</html>
```
Now inside of our python code just change that return and use the function `render_template`.
```
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('hello.html')
```
Now flask render this html files in a special way, because uses something called "jinj2" which is able to render and mix some python code inside of a html thats sounds good no ?, so lets see if we can import the ipv address user inside of the html, firstly we need to add another argument to the `render_template` function, like this.
```
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def root():
    # Get the ip address
    user_ip = request.remote_addr
    
    # Rendering htmls
    return render_template('hello.html', user_ip = user_ip)
```
Inside of our html, we need to use the jinja2 syntax like this, if we want to print some variable we use `{{ my var }}`.
```
<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <h1>Hello There, this is your ip {{ user_ip }}</h1>
    </body>
</html>
```
Te result is this.
![alt text](./ip.png)


