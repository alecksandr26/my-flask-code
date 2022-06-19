# Simple Todo list
Its a simple project where I used all the learned things from flask, jinja2 and sqlalchemy.
## Create the virtual env and build
When you create the virtualenv you will need to install the requirements, so just run.
```
$ pip install -r requirements.txt
```
## DataBase for the aplication 
I'm using gcloud with a simple firebase to manipulate and save the data from the users and todos, then you can install and configure the `google sdk` easily here on this link [google sdk](https://cloud.google.com/sdk/docs/install-sdk) here is a simple page to see how it works [firebase](https://firebase.google.com/docs/firestore?hl=es-419) and at the end you will need to create a service to be able to access creating this service you will get a `key.json` to be able to connect successful, link with more details [link](https://cloud.google.com/docs/authentication/getting-started).<br />
## .env file
You will need to create an `.env` inside of this file you will need to put the path of your `key.json`.
```
KEY_JSON="path_to_your_key.json"
```
