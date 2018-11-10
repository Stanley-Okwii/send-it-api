from app.common.data import user_list
from flask import request
from flask_restful import abort
import re

def get_specific_user(email):
    return next((item for item in user_list if item["email"] == email), False)

def abort_if_user_does_not_exist(email):
    user = get_specific_user(email)
    if user == False:
        abort(404, message="user with email {0} doesn't exist".format(email))

def abort_if_content_type_is_not_json():
    if request.content_type != 'application/json':
        abort(400, message="content-type must be json")

def abort_if_email_does_not_match_type_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        abort(400, message="missing or incorrect email format")

def abort_if_password_is_less_than_4_characters(password):
    if len(password) < 4:
        abort(400, message="password is missing or less than 4 characters")
   
