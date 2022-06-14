# Dealing with forms
To deal with forms in flask there is an extesion that we should use called `flask wtf`, to install this extesion just run.
```
$ pip install flask-wtf
```
Now we are ready to work with that extesion, we just include `FlaskForm` to work with forms, and to play with this module, we only need to create a new class inherited from `FlaskForm` like this.
```
"""
We are going to create a simple login 
"""

from flask import Flask, request, make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)
bootstrap  = Bootstrap(app)

app.config["SECRET_KEY"] = 'mykey'

class LoginForm(FlaskForm):
    pass

@app.route('/')
def index():
    return 'hello'
```
Inside of this class we are going to encapsulate all the variables that we want to receive from the form, for do that we need to import some functions, we need that functions because they are going to help us to create that reference so just take a look this code.
```
"""
We are going to create a simple login 
"""

from flask import Flask, request, make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap

# import the flask class
from flask_wtf import FlaskForm
# The reference functions
from wtforms.fields import StringField, PasswordField


app = Flask(__name__)
bootstrap  = Bootstrap(app)

app.config["SECRET_KEY"] = 'mykey'

class LoginForm(FlaskForm):
    username = StringField("User name")
    password = PasswordField("User password")
    

@app.route('/')
def index():
    return 'hello'
```
Another thing that we should add are validators, why, because we want to receive good forms and not bad forms, thats an important thing creating good code, so to add a validator to this form we need to import another class called `DataRequired`.
```
"""
We are going to create a simple login 
"""

from flask import Flask, request, make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap

# import the flask class
from flask_wtf import FlaskForm
# The reference functions
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap  = Bootstrap(app)

app.config["SECRET_KEY"] = 'mykey'

class LoginForm(FlaskForm):
    username = StringField("User name")
    password = PasswordField("User password")
    

@app.route('/')
def index():
    return 'hello'
```
Now inside of each Field we must to add an instance of `DataRequired` this validator will obligate the user to fill obligatory that field, so to add it we only need to create a list and do something like this.
```
"""
We are going to create a simple login 
"""

from flask import Flask, request, make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap

# import the flask class
from flask_wtf import FlaskForm
# The reference functions
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap  = Bootstrap(app)

app.config["SECRET_KEY"] = 'mykey'

class LoginForm(FlaskForm):
    username = StringField("User name", validators = [DataRequired()])
    password = PasswordField("User password", validators = [DataRequired()])
    

@app.route('/')
def index():
    return 'hello'
```
To finish with this form we should add `submit` button, to add that thing to our form we only need to include that field from the fields module liket this.
```
"""
We are going to create a simple login 
"""

from flask import Flask, request, make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap

# import the flask class
from flask_wtf import FlaskForm
# The reference functions
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap  = Bootstrap(app)

app.config["SECRET_KEY"] = 'mykey'

class LoginForm(FlaskForm):
    username = StringField("User name", validators = [DataRequired()])
    password = PasswordField("User password", validators = [DataRequired()])
    submit = SubmitField('Send')
    

@app.route('/')
def index():
    return 'hello'
```
# Creating the form in bootstrap
We have ready the logic in flask but now we are going to create the form in bootstrap, I create my base tample like this.
```
{% extends 'bootstrap/base.html' %}

{% block head %}
{{ super() }}
<title>Example of login</title>

{% endblock %}

{% block body %}
<h1>Example of a loing</h1>

{% endblock %}
```
After that I create another template that are an extesion of the base template, inside of this tampleate I import the bootstrap login component.
```
{% extends 'base.html' %}

{% block body %}
{{ super() }}

<p>Welcome to the loing page</p>

{% endblock %}
```
And also I create a home template like this.
```
{% extends 'base.html' %}


{% block body %}
{{ super() }}

<p>Welcome to home</p>

{% endblock %}
```
And I modify a little bit the flask code I add a login path like this.
```
"""
We are going to create a simple login 
"""

from flask import Flask, request, make_response, session, redirect, render_template
from flask_bootstrap import Bootstrap

# import the flask class
from flask_wtf import FlaskForm
# The reference functions
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap  = Bootstrap(app)

app.config["SECRET_KEY"] = 'mykey'

class LoginForm(FlaskForm):
    username = StringField("User name", validators = [DataRequired()])
    password = PasswordField("User password", validators = [DataRequired()])
    submit = SubmitField('Send')

@app.route('/login')
def login():
    return render_template('login.html')
    

@app.route('/')
def index():
    if not session.get('user'):
        response = make_response(redirect('/login'))
        return response
    
    return render_template('home.html')
```
Then lets create our form I create two versions, becasue the wtf module adds another base.html with some macros that we can use to import some components, I decided to add the two methods.
```
{% extends 'base.html' %}

<!-- Includes the quick_form -->
{% import 'bootstrap/wtf.html' as wtf %}

{% block body %}
{{ super() }}
<!-- This is the block of code of container -->
<h2>First way</h2>
<div class="container">
    <!-- This is the way how we can create a simple form  -->
    <form action="{{ url_for('login') }}" method='POST'>
        {{ login_form.username.label }}
        {{ login_form.username }}
        <br />
        {{ login_form.password.label }}
        {{ login_form.password }}
        <br />
        {{ login_form.submit }}
        
    </form>
</div>

<h2>Second way</h2>

<div class="container">
    <!-- This is the way how we can create a simple form  -->
    <form action="{{ url_for('login') }}" method='POST'>
      {{ wtf.quick_form(login_form) }}
    </form>
</div>

{% endblock %}
```

