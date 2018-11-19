from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from app.common.store import parcel_delivery_orders
from app.common.util import (
    get_specific_user,
    abort_if_user_does_not_exist,
    abort_if_email_does_not_match_type_email,
    abort_if_password_is_less_than_4_characters,
    abort_if_user_does_not_have_orders,
    abort_if_parcel_does_not_exist,
    get_specific_parcel,
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
            'id': args['id'],
            'parcel': args['parcel'],
            'weight': args['weight'],
            'price': args['price'],
            'receiver': args['receiver'],
            'pickup_location': args['pickup_location'],
            'destination': args['destination'],
            'current_location': args['pickup_location'],
            'status': 'pending',
            }
        parcel_delivery_orders[email].append(newOrder)

        return response('parcel delivery order successfully created', 201)

    @jwt_required
    def get(self, email):
        abort_if_attribute_is_empty("email", email)
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        user = get_specific_user(email)
        if(user['role'] == 'admin'): 
            flattened_list = [parcel_order
                for sub_list in parcel_delivery_orders.values()
                for parcel_order in sub_list]
            return process_response_data(flattened_list, 200) 
        else: 
            abort_if_user_does_not_have_orders(email)
            return process_response_data(parcel_delivery_orders[email], 200)

    @jwt_required
    def put(self):
        abort_if_content_type_is_not_json()
        args = request.get_json()
        abort_if_user_input_is_missing(args, ['email','id'])
        email = args['email']
        orderId = args['id']
        abort_if_user_does_not_exist(email)
        abort_if_user_does_not_have_orders(email)
        orderlist = parcel_delivery_orders[email]
        abort_if_parcel_does_not_exist(email, orderId)
        currentOrder = get_specific_parcel(email,orderId)
        newOrder = {
            'id': currentOrder['id'],
            'parcel': currentOrder['parcel'],
            'weight': currentOrder['weight'],
            'price': currentOrder['price'],
            'receiver': currentOrder['receiver'],
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
        orderlist[orderlist.index(currentOrder)] = newOrder
        parcel_delivery_orders[email].append(newOrder)

        return response('parcel has been successfully updated', 201)

class UserParcelOrder(MethodView):
    @jwt_required
    def get(self, orderId):
        if(len(str(orderId)) > 0 and str(orderId).isnumeric()):
            flattened_list = [parcel_order
                for sub_list in parcel_delivery_orders.values()
                for parcel_order in sub_list]
            single_parcel = next((parcel for parcel in flattened_list if parcel["id"] == orderId), False)
            if single_parcel:
                return process_response_data(single_parcel, 200)
            else:
                return response("parcel order with id {0} does not exist".format(orderId), 404)
        else:
            return response("parcel order must be numeric ", 404)

