from app.common.store import user_list, parcel_delivery_orders
from flask_restful import abort, reqparse
import re

def get_specific_user(email):
    return next((item for item in user_list if item["email"] == email), False)

def abort_if_user_does_not_exist(email):
    user = get_specific_user(email)
    if user == False:
        abort(404, message="user with email {0} doesn't exist".format(email))

def abort_if_email_does_not_match_type_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        abort(400, message="missing or incorrect email format")

def abort_if_password_is_less_than_4_characters(password):
    if (len(str(password)) < 4):
        abort(400, message="password is missing or less than 4 characters")

def get_specific_parcel(email, orderId):
    return next((item for item in parcel_delivery_orders[email] if item["id"] == orderId), False)

def abort_if_parcel_does_not_exist(email, orderId):
    parcel = get_specific_parcel(email, orderId)
    if parcel == False:
        abort(404, message="parcel order with id {0} does not exist".format(orderId))

def abort_if_user_does_not_have_orders(email):
    if (len(parcel_delivery_orders[email]) == 0):
        abort(404, message="User with email {} does not have any orders".format(email))
