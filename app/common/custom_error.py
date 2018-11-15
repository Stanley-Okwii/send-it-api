from app import api
from app.common.util import response

@api.errorhandler(404)
def route_not_found(e):
    return response('The requested endpoint was not found', 404)

@api.errorhandler(405)
def method_not_found(e):
    return response('The method is not allowed for the requested URL', 405)
