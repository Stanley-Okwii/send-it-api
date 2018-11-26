from flask import jsonify, request
from flasgger import swag_from
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db_methods import (
    register_new_user,
    update_user_account,
    update_user_role_to_admin,
    delete_user_account,
    get_all_users
    )
from app.common.util import (
    response,
    process_response_data,
    abort_if_email_does_not_match_type_email,
    abort_if_user_does_not_exist,
    get_specific_user,
    abort_if_password_is_less_than_4_characters,
    abort_if_user_already_exists,
    abort_if_attribute_is_empty,
    abort_if_user_input_is_missing,
    abort_if_content_type_is_not_json
    )


class Welcome(MethodView):
    def get(self):
        return response('welcome to send it api v1', 200)


class UserList(MethodView):
    @jwt_required
    @swag_from('../docs/admin_view_users.yml')
    def get(self):
        user = get_jwt_identity()
        users = get_all_users()
        if(user['role'] == 'admin'):
            return process_response_data(users, 200)
        else:
            return response(
                'you do not have permission to access this endpoint',
                401)


class Admin(MethodView):
    @jwt_required
    @swag_from('../docs/admin_update_role.yml')
    def put(self):
        arguments = request.get_json()
        abort_if_user_input_is_missing(arguments, ['email', 'role'])
        abort_if_content_type_is_not_json()
        email = arguments['email']
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_does_not_exist(email)
        role = arguments['role']
        abort_if_attribute_is_empty('role', role)
        user = get_jwt_identity()
        if(user['role'] == 'admin'):
            user_details = {
                'email': email,
                'role': role
            }
            update_user_role_to_admin(user_details)
            return response('user role changed to {}'.format(role), 200)
        else:
            return response(
                'you do not have permission to access this endpoint',
                401)


class User(MethodView):
    @jwt_required
    @swag_from('../docs/user_details.yml')
    def get(self):
        user = get_jwt_identity()
        response = get_specific_user(user['email'])

        return process_response_data(response, 200)

    @jwt_required
    @swag_from('../docs/delete_user.yml')
    def delete(self):
        user = get_jwt_identity()
        delete_user_account(email=user['email'])

        return response('user account deleted', 200)

    @jwt_required
    @swag_from('../docs/edit_user.yml')
    def put(self):
        user = get_jwt_identity()
        abort_if_content_type_is_not_json()
        arguments = request.get_json()
        abort_if_user_input_is_missing(arguments, ['name', 'password'])
        name = arguments['name']
        abort_if_attribute_is_empty('name', name)
        password = arguments['password']
        abort_if_password_is_less_than_4_characters(password)
        newUser = {
            'username': name,
            'password': password
            }
        update_user_account(email=user['email'], data=newUser)

        return response('successfully updated account details', 201)

    @swag_from('../docs/sign_up.yml')
    def post(self):
        abort_if_content_type_is_not_json()
        arguments = request.get_json()
        abort_if_user_input_is_missing(arguments, ['name', 'email', 'password'])
        name = arguments['name']
        email = arguments['email']
        password = arguments['password']
        abort_if_attribute_is_empty('name', name)
        abort_if_email_does_not_match_type_email(email)
        abort_if_user_already_exists(email, name)
        abort_if_password_is_less_than_4_characters(password)
        if email == 'admin@gmail.com':
            role = 'admin'
        else:
            role = 'user'

        newUser = {
            'username': name,
            'email': email,
            'password': password,
            'role': role
            }
        register_new_user(data=newUser)

        return response('successfully created new account', 201)
