from flask import Flask
from flask_restful import reqparse, Resource
from app.helpers.data import user_list
from app.helpers.views import get_specific_user, abort_if_user_does_not_exist

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('password')

class Welcome(Resource):
    def get(self):
        return "welcome to send it api v1", 200

class UserList(Resource):
    def get(self):
        return user_list, 200

class User(Resource):
    def get(self, email):
        abort_if_user_does_not_exist(email)
        return get_specific_user(email), 200

    def delete(self, email):
        abort_if_user_does_not_exist(email)
        user_to_delete = get_specific_user(email)
        user_list.remove(user_to_delete)
        del user_to_delete
        return '', 204

    def put(self, email):
        user = get_specific_user(email)
        abort_if_user_does_not_exist(email)
        args = parser.parse_args()
        newUser = { 'name': args['name'], "email": user["email"], "password": args["password"] }
        user_list[user_list.index(user)] = newUser

        return newUser, 201

    def post(self):
        args = parser.parse_args()
        newUser = { 'name': args['name'], "email": args["email"], "password": args["password"] }
        user_list.append(newUser)

        return newUser, 201
