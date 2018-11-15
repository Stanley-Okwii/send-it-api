from flask import jsonify, request
from flask.views import MethodView
from app.common.store import user_list, parcel_delivery_orders
from app.common.util import (
    response,
    process_response_data,
    abort_if_email_does_not_match_type_email,
    abort_if_user_does_not_exist,
    get_specific_user,
    abort_if_password_is_less_than_4_characters,
    abort_if_user_already_exists,
    abort_if_attribute_is_empty,
    abort_if_user_input_is_missing
    )

class Welcome(MethodView):
    def get(self):
        return response("welcome to send it api v1", 200)

class UserList(MethodView):
    def get(self, email):
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        user = get_specific_user(email)
        if(user['role'] == 'admin'):
            return process_response_data(user_list, 200)
        else:
            return response("you do not have permission to access this endpoint", 404)

class User(MethodView):
    def get(self, email):
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        response = get_specific_user(email)

        return process_response_data(response, 200)

    def delete(self, email):
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        user_to_delete = get_specific_user(email)
        user_list.remove(user_to_delete)

        return response("user account deleted", 204)

    def put(self, email):
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        user = get_specific_user(email)
        args = request.get_json()
        abort_if_user_input_is_missing(args, ["name", "password"])
        name = args['name']
        abort_if_attribute_is_empty("name", name)
        password = args['password']
        abort_if_password_is_less_than_4_characters(password)
        newUser = { 'name': name, "email": user["email"], "password": password, 'role': user['role'] }
        user_list[user_list.index(user)] = newUser

        return response("successfully updated account details", 201)

    def post(self):
        args = request.get_json()
        abort_if_user_input_is_missing(args, ["name","email","password", "role"])
        name = args['name']
        email = args['email']
        role = args['role']
        password = args['password']
        abort_if_attribute_is_empty("name", name)
        abort_if_attribute_is_empty("role", role)
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_already_exists(email)
        abort_if_password_is_less_than_4_characters(password)
        newUser = { 'name': name, "email": email, "password": password,'role': role }
        user_list.append(newUser)
        parcel_delivery_orders[newUser["email"]] = []

        return response("successfully created new user account", 201)
