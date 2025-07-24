from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel:
    def __init__(self, mongo):
        self.users = mongo.db.users  # Should reference 'users' collection, not 'tasks'

    def create_user(self, username, password):
        hashed_password = generate_password_hash(password)
        self.users.insert_one({
            "username": username,
            "password": hashed_password
        })

    def find_by_username(self, username):
        return self.users.find_one({"username": username})

    def verify_user(self, username, password):
        user = self.find_by_username(username)
        if user and check_password_hash(user["password"], password):
            return True
        return False
