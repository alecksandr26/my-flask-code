"""
To create the model of a user with the required properties that flask_login needs
"""

# This kind of modes is already implemented by flask_login
# So Here I imported that model and inherited
from flask_login import UserMixin

# To get a user in a very simple way just returning the id
from app.firestore_service import get_user_by_id

# To save the data
class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        


class UserModel(UserMixin):
    def __init__(self, user_data : UserData):
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id):
        user_doc = get_user_by_id(user_id = user_id)

        user_data = UserData(
            username = user_doc.id,
            password = user_doc.to_dict()['password']
        )

        return UserModel(user_data)
        
        






