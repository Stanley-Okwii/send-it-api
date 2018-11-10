from flask import Flask
from flask_restful import Api
from app.auth.views import User, UserList, Welcome

app = Flask(__name__)
api = Api(app)

api.add_resource(UserList, "/api/v1/users")
api.add_resource(Welcome, "/api/v1", "/")
api.add_resource(User, '/api/v1/user/<email>', '/api/v1/user')
