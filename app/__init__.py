from flask import Flask
from flask_restful import Api
from app.auth.views import User, UserList, Welcome
from app.send_it.sign_in import SignIn
from app.send_it.parcel_delivery import ParcelDeliveryOrder

app = Flask(__name__)
api = Api(app)

api.add_resource(UserList, "/api/v1/users")
api.add_resource(Welcome, "/api/v1", "/")
api.add_resource(User, '/api/v1/user/<email>', '/api/v1/user')
api.add_resource(SignIn, '/api/v1/auth/signin')
api.add_resource(ParcelDeliveryOrder, "/api/v1/parcels")
