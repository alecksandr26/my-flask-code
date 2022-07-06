"""
Our data base are going to be a simple firebase
So you need to buuil
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)


db = firestore.client()


# Return all the users as a objects
def get_users():
    return db.collection('users').get()


# Return a user by id from the data base if exist else return None
def get_user_by_id(user_id):
    return db.collection('users').document(user_id).get()


# Return all the todos from a user
def get_todos_from_user(user_id):
    return db.collection('users').document(user_id).collection('todos').get()



