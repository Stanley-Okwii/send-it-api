from flask import Flask
from app.auth.views import Welcome, User, UserList, Admin
from app.models import DataModel
from app.common.util import response
from app.send_it.sign_in import SignIn
from app.send_it.archive_parcels import ArchiveParcels
from app.send_it.parcel_delivery import (
    ParcelDeliveryOrder,
    UserParcelOrder,
    CancelParcel,
    ParcelDestination,
    ParcelStatus,
    ParcelCurrentLocation
    )
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

api.config['JWT_SECRET_KEY'] = 'Abracadabra'
api.config['SWAGGER'] = {
    'title': 'SEND IT API',
    'uiversion': 3,
    'description': 'A set of API endpoints to provide and manipulate data for the SendIT courier services',
}

swagger = Swagger(api)

jwt = JWTManager(api)

db = DataModel()
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
parcel_current_location_view = ParcelCurrentLocation.as_view('parcel_current_location_view')
parcel_archive_view = ArchiveParcels.as_view('parcel_archive_view')

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
    methods=['POST', 'GET']
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
    "/api/v1/parcels/current_location",
    view_func=parcel_current_location_view,
    methods=['PUT']
    )
api.add_url_rule(
    "/api/v1/parcels/status",
    view_func=parcel_status_view,
    methods=['PUT']
    )
api.add_url_rule("/api/v1/role", view_func=admin_view, methods=['PUT'])
api.add_url_rule("/api/v1/archive", view_func=parcel_archive_view, methods=['GET'])

