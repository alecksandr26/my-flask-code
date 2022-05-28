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
