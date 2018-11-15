from flask import Flask
from app.auth.views import Welcome, User, UserList
from app.common.util import response
from app.send_it.sign_in import SignIn
from app.send_it.parcel_delivery import ParcelDeliveryOrder, UserParcelOrder

api = Flask(__name__)

# Register classes as views
welcome_view = Welcome.as_view('welcome')
user_view = User.as_view('user')
user_list_view = UserList.as_view('user_list')
sign_in_view = SignIn.as_view('sign_in')
parcel_delivery_order_view = ParcelDeliveryOrder.as_view('parcel_delivery_order')
user_parcel_order_view = UserParcelOrder.as_view('user_parcel_view')

# import views with custom error messages
from app.common import views

# Add url rules endpoints
api.add_url_rule('/api/v1', view_func=welcome_view, methods=['GET'])
api.add_url_rule('/', view_func=welcome_view, methods=['GET'])
api.add_url_rule("/api/v1/user/<email>", view_func=user_view, methods=['GET', 'DELETE', 'PUT'])
api.add_url_rule("/api/v1/user", view_func=user_view, methods=['POST'])
api.add_url_rule("/api/v1/users",  view_func=user_list_view, methods=['GET'])
api.add_url_rule("/api/v1/auth/signin",  view_func=sign_in_view, methods=['POST'])
api.add_url_rule("/api/v1/parcels",  view_func=parcel_delivery_order_view, methods=['POST', 'GET','PUT'])
api.add_url_rule("/api/v1/users/<email>/parcels", view_func=parcel_delivery_order_view, methods=['GET'])
api.add_url_rule("/api/v1/parcels/<orderId>",
                 view_func=user_parcel_order_view, methods=['GET'])
