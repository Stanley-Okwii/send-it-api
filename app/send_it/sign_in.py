from flask import jsonify, request
from flasgger import swag_from
from flask.views import MethodView
from app.common.util import (
    get_specific_user,
    abort_if_user_does_not_exist,
    abort_if_email_does_not_match_type_email,
    abort_if_password_is_less_than_4_characters,
    response,
    abort_if_content_type_is_not_json,
    abort_if_user_input_is_missing,
    abort_if_attribute_is_empty,
    process_response_data
    )
from flask_jwt_extended import (
    create_access_token
    )

class SignIn(MethodView):
    @swag_from('../docs/sign_in.yml')
    def post(self):
        abort_if_content_type_is_not_json()
        args = request.get_json()
        abort_if_user_input_is_missing(args, ["email", "password"])
        password = args['password']
        email = args['email']
        abort_if_attribute_is_empty("email", email)
        abort_if_attribute_is_empty("password", password)
        abort_if_email_does_not_match_type_email(email)
        abort_if_password_is_less_than_4_characters(password)
        abort_if_user_does_not_exist(email)
        user = get_specific_user(email)
        user_identity = {
            'name': user['username'],
            'email': user['email'],
            'role': user['role']
            }
        access_token = create_access_token(identity = user_identity)
        user_response = {
                'message': 'You have logged in successfully.',
                'user_token': access_token
                }
        if user['password'] == password:
            return process_response_data(user_response, 200)
        else:
            return response('Invalid email or password, Please try again', 401)
