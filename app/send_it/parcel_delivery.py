from flask import jsonify, request
from flask.views import MethodView
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
    process_response_data
    )

class ParcelDeliveryOrder(MethodView):
    def post(self):
        email = request.args.get('email')
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        newOrder = {
            "id": request.args.get('id'),
            "parcel": request.args.get('parcel'),
            "weight": request.args.get('weight'),
            "price": request.args.get('price'),
            "receiver": request.args.get('receiver'),
            "pickup_location": request.args.get('pickup_location'),
            "destination": request.args.get('destination'),
            "current_location": request.args.get('pickup_location'),
            "status": "pending",
            }
        parcel_delivery_orders[email].append(newOrder)

        return response("parcel delivery order successfully created", 201)

    def get(self, email=None):
        if(email):
            abort_if_email_does_not_match_type_email(email)
            abort_if_user_does_not_exist(email)
            abort_if_user_does_not_have_orders(email)
            return process_response_data(parcel_delivery_orders[email], 200)
        else:
            flattened_list = [parcel_order
                for sub_list in parcel_delivery_orders.values()
                for parcel_order in sub_list]
            return process_response_data(flattened_list, 200)

    def put(self):
        email = request.args.get('email')
        orderId = request.args.get('id')
        abort_if_user_does_not_exist(email)
        abort_if_user_does_not_have_orders(email)
        orderlist = parcel_delivery_orders[email]
        abort_if_parcel_does_not_exist(email, orderId)
        currentOrder = get_specific_parcel(email,orderId)
        location_update = request.args.get('current_location')
        destination_update = request.args.get('destination')
        status_update = request.args.get("status")
        newOrder = {
            "id": currentOrder['id'],
            "parcel": currentOrder['parcel'],
            "weight": currentOrder['weight'],
            "price": currentOrder['price'],
            "receiver": currentOrder['receiver'],
            "pickup_location": currentOrder['pickup_location'],
            "destination": destination_update
                if destination_update
                else currentOrder['destination'],
            "current_location": location_update
                if location_update
                else currentOrder['current_location'],
            "status": status_update
                if status_update
                else currentOrder['status']
            }
        orderlist[orderlist.index(currentOrder)] = newOrder
        parcel_delivery_orders[email].append(newOrder)
        return response("parcel has been successfully updated", 201)

class UserParcelOrder(MethodView):
    def get(self, email, orderId):
        if((len(str(orderId)) > 0) and email):
            abort_if_email_does_not_match_type_email(email)
            abort_if_user_does_not_have_orders(email)
            abort_if_user_does_not_exist(email)
            abort_if_parcel_does_not_exist(email, orderId)
            single_parcel = get_specific_parcel(email, orderId)

        return process_response_data(single_parcel, 200)
