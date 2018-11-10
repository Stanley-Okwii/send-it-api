from flask import Flask
from flask_restful import reqparse, Resource
from app.common.data import user_list
from app.common.util import get_specific_user, \
    abort_if_user_does_not_exist, \
    abort_if_email_does_not_match_type_email, \
    abort_if_password_is_less_than_4_characters

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('password')

class Welcome(Resource):
    def get(self):
        return { "message": "welcome to send it api v1" }, 200

class UserList(Resource):
    def get(self):
        return user_list, 200

class User(Resource):
    def get(self, email):
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)

        return get_specific_user(email), 200

    def delete(self, email):
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        user_to_delete = get_specific_user(email)
        user_list.remove(user_to_delete)

        return { "message": "user account deleted" }, 204

    def put(self, email):
        abort_if_email_does_not_match_type_email(email)
        user = get_specific_user(email)
        abort_if_user_does_not_exist(email)
        args = parser.parse_args()
        password = args["password"]
        abort_if_password_is_less_than_4_characters(password)
        newUser = { 'name': args['name'], "email": user["email"], "password": password }
        user_list[user_list.index(user)] = newUser

        return { "message": "successfully updated account details" }, 201



    def post(self):
        args = parser.parse_args()
        abort_if_email_does_not_match_type_email(args["email"])
        abort_if_password_is_less_than_4_characters(args["password"])
        newUser = { 'name': args['name'], "email": args["email"], "password": args["password"] }
        user_list.append(newUser)

        return { "message": "successfully created new user account"}, 201
