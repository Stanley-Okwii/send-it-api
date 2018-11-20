from flask import jsonify, request
from flask.views import MethodView
from werkzeug.security import check_password_hash
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
        is_password_matched = check_password_hash(user['password'], password)
        access_token = create_access_token(identity = user)
        user_response = {
                'message': 'You have logged in successfully.',
                'user_token': access_token
                }
        if is_password_matched:
            return response('Invalid email or password, Please try again', 401)
        else:
            return process_response_data(user_response, 200)
