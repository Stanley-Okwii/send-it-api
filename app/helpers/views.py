from app.helpers.data import user_list
from flask_restful import reqparse, abort

def get_specific_user(email):
    return next((item for item in user_list if item["email"] == email), False)

def abort_if_user_does_not_exist(email):
    user = get_specific_user(email)
    if user == False:
        abort(404, message="User with email {0} doesn't exist".format(email))
