from flask import Flask
from flask_restful import reqparse, Resource
from app.common.store import user_list
from app.common.util import get_specific_user, \
    abort_if_user_does_not_exist, \
    abort_if_email_does_not_match_type_email, \
    abort_if_password_is_less_than_4_characters

parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('password')

class SignIn(Resource):
    def post(self):
        args = parser.parse_args()
        password = args["password"]
        email = args["email"]
        abort_if_email_does_not_match_type_email(email)
        abort_if_password_is_less_than_4_characters(password)
        abort_if_user_does_not_exist(email)
        user = get_specific_user(email)
        if (user['password'] == password):
            return { 'message': 'You logged in successfully.' }, 200
        else:
            return { 'message': 'Invalid email or password, Please try again' }, 401
