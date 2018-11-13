from flask import jsonify, request
from flask.views import MethodView
from app.common.store import user_list
from app.common.util import (
    get_specific_user,
    abort_if_user_does_not_exist,
    abort_if_email_does_not_match_type_email,
    abort_if_password_is_less_than_4_characters,
    response
    )

class SignIn(MethodView):
    def post(self):
        password = request.args.get('password')
        email = request.args.get('email')
        abort_if_email_does_not_match_type_email(email)
        abort_if_password_is_less_than_4_characters(password)
        abort_if_user_does_not_exist(email)
        user = get_specific_user(email)
        if (user['password'] == password):
            return response('You logged in successfully.', 200)
        else:
            return response('Invalid email or password, Please try again', 401)
