from flask import jsonify, request
from flasgger import swag_from
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db_methods import get_all_parcel_orders
from app.common.util import (
    response,
    process_response_data
    )


class ArchiveParcels(MethodView):
    @jwt_required
    @swag_from('../docs/get_parcels.yml')
    def get(self):
        user = get_jwt_identity()
        if(user['role'] == 'admin'):
            parcel_list = get_all_parcel_orders('parcel_order_archive')
            return process_response_data(parcel_list, 200)
        else:
            return response("you are not authorized to access this endpoint", 404)
