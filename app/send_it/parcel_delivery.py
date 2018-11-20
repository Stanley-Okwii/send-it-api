from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db_methods import create_parcel_order, get_all_parcel_orders, update_parcel_order
from app.common.util import (
    get_specific_user,
    abort_if_user_does_not_exist,
    abort_if_email_does_not_match_type_email,
    abort_if_password_is_less_than_4_characters,
    abort_if_user_does_not_have_orders,
    abort_if_parcel_does_not_exist,
    get_specific_parcel_by_id,
    get_parcels_by_email,
    response,
    process_response_data,
    abort_if_parcel_input_is_missing,
    abort_if_parcel_input_is_not_valid,
    abort_if_content_type_is_not_json,
    abort_if_attribute_is_empty,
    abort_if_user_input_is_missing
    )

class ParcelDeliveryOrder(MethodView):
    @jwt_required
    def post(self):
        args = request.get_json()
        abort_if_content_type_is_not_json()
        abort_if_parcel_input_is_missing(args)
        abort_if_parcel_input_is_not_valid(args)
        email = args['email']
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        newOrder = {
            'parcel': args['parcel'],
            'weight': args['weight'],
            'price': args['price'],
            'receiver': args['receiver'],
            'pickup_location': args['pickup_location'],
            'destination': args['destination'],
            'current_location': args['pickup_location'],
            'email': email
            }
        create_parcel_order(newOrder)

        return response('parcel delivery order successfully created', 201)

    @jwt_required
    def get(self):
        args = request.get_json()
        abort_if_content_type_is_not_json()
        email = args['email']
        abort_if_attribute_is_empty("email", email)
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        user = get_jwt_identity()
        if(user['role'] == 'admin'): 
            parcel_list = get_all_parcel_orders()
            return process_response_data(parcel_list, 200) 
        else: 
            abort_if_user_does_not_have_orders(email)
            user_orders = get_parcels_by_email(email)
            return process_response_data(user_orders, 200)

    @jwt_required
    def put(self):
        abort_if_content_type_is_not_json()
        args = request.get_json()
        abort_if_user_input_is_missing(args, ['id'])
        orderId = args['id']
        abort_if_parcel_does_not_exist(orderId)
        currentOrder = get_specific_parcel_by_id(orderId)
        order_update = {
            'order_id': currentOrder['order_id'],
            'pickup_location': currentOrder['pickup_location'],
            'destination': args['destination']
                if 'destination' in args.keys()
                else currentOrder['destination'],
            'current_location': args['current_location']
                if 'current_location' in args.keys()
                else currentOrder['current_location'],
            'status':  args['status']
                if 'status' in args.keys()
                else currentOrder['status']
            }
        update_parcel_order(data=order_update)

        return response('parcel has been successfully updated', 201)

class UserParcelOrder(MethodView):
    @jwt_required
    def get(self, orderId):
        if(len(str(orderId)) > 0 and str(orderId).isnumeric()):
            single_parcel = get_specific_parcel_by_id(orderId)
            if single_parcel:
                return process_response_data(single_parcel, 200)
            else:
                return response("parcel order does not exist", 404)
        else:
            return response("parcel order must be numeric ", 404)

