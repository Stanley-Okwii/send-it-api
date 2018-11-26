from flask import jsonify, request
from flasgger import swag_from
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db_methods import (
    create_parcel_order,
    get_all_parcel_orders,
    update_parcel_order
    )
from app.common.util import (
    abort_if_user_does_not_have_orders,
    abort_if_user_does_not_own_order,
    abort_if_parcel_does_not_exist,
    get_specific_parcel_by_id,
    get_parcels_by_email,
    response,
    process_response_data,
    abort_if_parcel_input_is_missing,
    abort_if_parcel_input_is_not_valid,
    abort_if_content_type_is_not_json,
    abort_if_user_input_is_missing
    )


class ParcelDeliveryOrder(MethodView):
    @jwt_required
    @swag_from('../docs/create_parcel.yml')
    def post(self):
        arguments = request.get_json()
        abort_if_content_type_is_not_json()
        abort_if_parcel_input_is_missing(arguments)
        abort_if_parcel_input_is_not_valid(arguments)
        user = get_jwt_identity()
        email = user['email']
        newOrder = {
                'parcel': arguments['parcel'],
                'weight': arguments['weight'],
                'price': arguments['price'],
                'receiver': arguments['receiver'],
                'pickup_location': arguments['pickup_location'],
                'destination': arguments['destination'],
                'current_location': arguments['pickup_location'],
                'email': email
                }
        create_parcel_order(newOrder)
        return response('parcel delivery order successfully created', 201)

    @jwt_required
    @swag_from('../docs/get_parcels.yml')
    def get(self):
        user = get_jwt_identity()
        if(user['role'] == 'admin'): 
            parcel_list = get_all_parcel_orders()
            return process_response_data(parcel_list, 200) 
        else: 
            abort_if_user_does_not_have_orders(user['email'])
            user_orders = get_parcels_by_email(user['email'])
            return process_response_data(user_orders, 200)


class UserParcelOrder(MethodView):
    @jwt_required
    @swag_from('../docs/get_a_parcel.yml')
    def get(self, orderId):
        if(len(str(orderId)) > 0 and str(orderId).isnumeric()):
            single_parcel = get_specific_parcel_by_id(orderId)
            if single_parcel:
                return process_response_data(single_parcel, 200)
            else:
                return response("parcel order does not exist", 400)
        else:
            return response("parcel order must be numeric ", 400)


class CancelParcel(MethodView):
    @jwt_required
    @swag_from('../docs/cancel_parcel.yml')
    def put(self):
        abort_if_content_type_is_not_json()
        arguments = request.get_json()
        abort_if_user_input_is_missing(arguments, ['id'])
        orderId = arguments['id']
        abort_if_parcel_does_not_exist(orderId)
        email = get_jwt_identity()['email']
        abort_if_user_does_not_own_order(email, orderId)
        currentOrder = get_specific_parcel_by_id(orderId)
        if currentOrder['status'] == 'delivered':
            return response('parcel order has already been delivered', 400)
        else:
            order_update = {
                'order_id': currentOrder['order_id'],
                'pickup_location': currentOrder['pickup_location'],
                'destination': currentOrder['destination'],
                'current_location': currentOrder['current_location'],
                'status': 'cancelled'
                }
            update_parcel_order(data=order_update)

        return response('parcel delivery has been cancelled', 201)


class ParcelDestination(MethodView):
    @jwt_required
    @swag_from('../docs/parcel_destination.yml')
    def put(self):
        abort_if_content_type_is_not_json()
        arguments = request.get_json()
        abort_if_user_input_is_missing(arguments, ['id', 'destination'])
        orderId = arguments['id']
        abort_if_parcel_does_not_exist(orderId)
        email = get_jwt_identity()['email']
        abort_if_user_does_not_own_order(email, orderId)
        currentOrder = get_specific_parcel_by_id(orderId)
        if currentOrder['status'] == 'delivered':
            return response('parcel order has already been delivered', 400)
        else:
            order_update = {
                'order_id': currentOrder['order_id'],
                'pickup_location': currentOrder['pickup_location'],
                'destination': arguments['destination'],
                'current_location': currentOrder['current_location'],
                'status': currentOrder['status']
                }
            update_parcel_order(data=order_update)

        return response('parcel delivery destination has been changed', 201)


class ParcelStatus(MethodView):
    @jwt_required
    @swag_from('../docs/parcel_status.yml')
    def put(self):
        abort_if_content_type_is_not_json()
        arguments = request.get_json()
        abort_if_user_input_is_missing(arguments, ['id'])
        orderId = arguments['id']
        role = get_jwt_identity()['role']
        abort_if_parcel_does_not_exist(orderId)
        currentOrder = get_specific_parcel_by_id(orderId)
        if currentOrder['status'] == 'delivered':
            return response('parcel order has already been delivered', 400)
        if role == 'admin':
            order_update = {
                'order_id': currentOrder['order_id'],
                'pickup_location': currentOrder['pickup_location'],
                'destination': currentOrder['destination'],
                'current_location': arguments['current_location']
                                    if 'current_location' in arguments.keys()
                                    else currentOrder['current_location'],
                'status': arguments['status']
                          if 'status' in arguments.keys()
                          else currentOrder['status']
                }
            update_parcel_order(data=order_update)

            return response('parcel delivery order has been updated', 201)
        else:
            return response("you are not authorized to edit order", 404)
