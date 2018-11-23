from app import api
from jwt import ExpiredSignatureError
from flask_jwt_extended.exceptions import NoAuthorizationError
from app.common.util import response

@api.errorhandler(404)
def route_not_found(e):
    return response('The requested endpoint was not found', 404)

@api.errorhandler(405)
def method_not_found(e):
    return response('The method is not allowed for the requested URL', 405)

@api.errorhandler(NoAuthorizationError)
def unauthorized_access(e):
    return response('Access denied, please provide a bearer token', 401)

@api.errorhandler(ExpiredSignatureError)
def expired_token(e):
    return response('Token has expired, generate a new token and try again', 400)
