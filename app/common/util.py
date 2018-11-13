from app.common.store import user_list, parcel_delivery_orders
from flask import abort, jsonify, make_response
import re

def response(message, status):
    return make_response(jsonify({
        'message': message
        })), status

def process_response_data(message, status):
    return make_response(jsonify(message)), status

def get_specific_user(email):
    return next((item for item in user_list if item["email"] == email), False)

def abort_if_user_does_not_exist(email):
    user = get_specific_user(email)
    if user == False:
        abort(make_response(jsonify(message="user with email {0} doesn't exist".format(email)), 404))

def abort_if_email_does_not_match_type_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        abort(make_response(jsonify(message="missing or incorrect email format"), 400))

def abort_if_password_is_less_than_4_characters(password):
    if (len(str(password)) < 4):
        abort(make_response(jsonify(message="password is missing or less than 4 characters"), 400))

def get_specific_parcel(email, orderId):
    return next((item for item in parcel_delivery_orders[email] if item["id"] == orderId), False)

def abort_if_parcel_does_not_exist(email, orderId):
    parcel = get_specific_parcel(email, orderId)
    if parcel == False:
        abort(make_response(jsonify(message="parcel order with id {0} does not exist".format(orderId)), 404))

def abort_if_user_does_not_have_orders(email):
    if (len(parcel_delivery_orders[email]) == 0):
        abort(make_response(jsonify(message="User with email {0} does not have any orders".format(email)), 404))
