from flask import Flask
from flask_restful import reqparse, Resource
from app.common.store import parcel_delivery_orders
from app.common.util import get_specific_user, \
    abort_if_user_does_not_exist, \
    abort_if_email_does_not_match_type_email, \
    abort_if_password_is_less_than_4_characters, \
    abort_if_user_does_not_have_orders, \
    abort_if_parcel_does_not_exist, \
    get_specific_parcel

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('parcel')
parser.add_argument('email')
parser.add_argument('weight', type=int, help='weight cannot be converted')
parser.add_argument('price')
parser.add_argument('receiver')
parser.add_argument('pickup_location')
parser.add_argument('destination')
parser.add_argument('current_location')
parser.add_argument('status')

class ParcelDeliveryOrder(Resource):
    def post(self):
        args = parser.parse_args()
        email = args["email"]
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        newOrder = {
            "id": args['id'],
            "parcel": args['parcel'],
            "weight": args['weight'],
            "price": args['price'],
            "receiver": args['receiver'],
            "pickup_location": args['pickup_location'],
            "destination": args['destination'],
            "current_location": args['pickup_location'],
            "status": "pending",
            }
        parcel_delivery_orders[email].append(newOrder)
        return {"message": "parcel delivery order successfully created"}, 201
