from app.common.store import user_list, parcel_delivery_orders
from app.models import DataModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort, jsonify, make_response, request
import re

db_connect = DataModel()
cursor = db_connect.cursor
dictcur = db_connect.dict_cursor

def response(message, status):
    return make_response(jsonify({
        'message': message
        })), status

def process_response_data(message, status):
    return make_response(jsonify(message)), status

def get_specific_user(email):
    query = "SELECT * FROM users WHERE email='{0}'".format(email)
    dictcur.execute(query)
    user = dictcur.fetchone()

    return user

def abort_if_user_does_not_exist(email):
    query = "SELECT * FROM users WHERE email='{0}'".format(email)
    dictcur.execute(query)
    user = dictcur.fetchone()
    if user == False:
        abort(make_response(jsonify(message="user doesn't exist".format(email)), 404))

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
        abort(make_response(jsonify(message="user does not have any orders"), 404))

def abort_if_attribute_is_empty(attribute, value):
    if value == "" or not value:
        abort(make_response(jsonify(message="attribute {0} or its value is missing".format(attribute)), 400))

def abort_if_user_already_exists(email):
    user = get_specific_user(email)
    if user:
        abort(make_response(jsonify(message="user already exists"), 400))

def abort_if_parcel_input_is_missing(parameter):
    parcel_details = ["email", "id", "parcel","weight", "price", "receiver", "pickup_location", "destination"]
    user_provided_attributes = parameter.keys()
    missing_attributes = list(set(parcel_details) - set(user_provided_attributes))
    if len(missing_attributes) > 0:
        abort(make_response(jsonify(
            message="attribute(s): {0} are missing".format(", ".join(missing_attributes))),
            400))

def abort_if_parcel_input_is_not_valid(parameter):
    for key, value in parameter.items():
        if(not value or value == ""):
            abort(make_response(
                jsonify(message="value of {0} is not have valid".format(key)),
                400))

def abort_if_content_type_is_not_json():
    if request.content_type != "application/json":
        abort(make_response(jsonify(message="content type must be application/json"), 400))

def abort_if_user_input_is_missing(parameter, details):
    user_provided_attributes = parameter.keys()
    missing_attributes = list(set(details) - set(user_provided_attributes))
    if len(missing_attributes) > 0:
        abort(make_response(jsonify(
            message="attribute(s): {0} are missing".format(", ".join(missing_attributes))),
            400))
