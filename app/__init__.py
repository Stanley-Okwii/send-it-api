import os
from flask import Flask
from app.auth.views import Welcome, User, UserList, Admin
from app.models import DataModel
from app.common.util import response
from app.send_it.sign_in import SignIn
from app.send_it.parcel_delivery import (
    ParcelDeliveryOrder,
    UserParcelOrder,
    CancelParcel,
    ParcelDestination,
    ParcelStatus
    )
from flask_jwt_extended import JWTManager

api = Flask(__name__)

api.config['JWT_SECRET_KEY'] = 'Abracadabra'
jwt = JWTManager(api)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
api.config.from_object(app_settings)

db =  DataModel()
db.create_user_table()
db.create_parcel_order_table()

# Register classes as views
welcome_view = Welcome.as_view('welcome')
user_view = User.as_view('user')
admin_view = Admin.as_view('admin')
user_list_view = UserList.as_view('user_list')
sign_in_view = SignIn.as_view('sign_in')
parcel_delivery_order_view = ParcelDeliveryOrder.as_view('parcel_delivery_order')
user_parcel_order_view = UserParcelOrder.as_view('user_parcel_view')
cancel_parcel_view = CancelParcel.as_view('cancel_parcel_view')
parcel_destination_view = ParcelDestination.as_view('parcel_destination_view')
parcel_status_view = ParcelStatus.as_view('parcel_status_view')

# import views with custom error messages
from app.common import custom_error

# Add url rules endpoints
api.add_url_rule('/api/v1', view_func=welcome_view, methods=['GET'])
api.add_url_rule('/', view_func=welcome_view, methods=['GET'])
api.add_url_rule(
    "/api/v1/user", view_func=user_view,
    methods=['GET', 'DELETE', 'PUT', 'POST']
    )
api.add_url_rule(
    "/api/v1/users",
    view_func=user_list_view,
    methods=['GET']
    )
api.add_url_rule(
    "/api/v1/auth/signin",
    view_func=sign_in_view,
    methods=['POST']
    )
api.add_url_rule(
    "/api/v1/parcels",
    view_func=parcel_delivery_order_view,
    methods=['POST', 'PUT', 'GET']
    )
api.add_url_rule(
    "/api/v1/parcels/<orderId>",
    view_func=user_parcel_order_view,
    methods=['GET']
    )
api.add_url_rule(
    "/api/v1/parcels/cancel",
    view_func=cancel_parcel_view,
    methods=['PUT']
    )
api.add_url_rule(
    "/api/v1/parcels/destination",
    view_func=parcel_destination_view,
    methods=['PUT']
    )
api.add_url_rule(
    "/api/v1/parcels/status",
    view_func=parcel_status_view,
    methods=['PUT']
    )
parcel_status_view
api.add_url_rule("/api/v1/role",
    view_func=admin_view,
    methods=['PUT']
    )
