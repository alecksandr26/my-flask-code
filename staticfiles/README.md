# Dealing with the static files 
Now to deal witht he static files like .png or .css for our pages, we need to create another folder called `static` this folder will contain all our css fiels and images files.
Then to load like a image inside of our html file we need to use `url_for`, and inside of our folder `static` I recommend to you to create an images folder.
Yeah, with this clear for exmpale this is my html file I just load a simple image.
```
<!DOCTYPE html>

<html>
    <head>
        <title>Static files</title>
    </head>
    <body>
        <h1>Static Files:</h1>
        <img src="{{ url_for('static', filename='img/Alecksandr.jpg') }}"  alt="wtf" />
    </body>
</html>
```
And the .py file is this, as you can see in `url_for` I pass as an argument the static folder where I put my image.
```
# This is an example of how we can manipulate static files in flask
from flask import Flask, render_template, request, url_for

# Here I define the path of the templates and static files
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html", url_for = url_for)
```
## Put css
To put css inside of a flask project it is recommend to create a folder inside of the `static` folder a folder witht the name `css`, so lets create `css` file, so in simple words to load a `css` file is very easy, go to your `base.html`, and just add a link inside of the head tag of your html file, like this.
```
<!DOCTYPE html>

<html>
    <head>
        <title>Static files</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}"></link>
    </head>
    <body>
        <h1>Static Files:</h1>
        <img src="{{ url_for('static', filename='img/Alecksandr.jpg') }}"  alt="wtf" />
    </body>
</html>
```
And yeah just like that we can add style to our html files, and this is my css file.
```
* {
    margin: 0px;
}

img {
    max-width: 200px;
}
```
