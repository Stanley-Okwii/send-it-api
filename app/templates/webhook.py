from app.common.util import response
from flask import request
from flask.views import MethodView

class WebHook(MethodView):
    def post(self):

        try:
            chan_id = request.args.get('X-Goog-Channel-ID', 'empty')
            msg_num = request.args.get('X-Goog-Message-Number', 'empty')
            rid = request.args.get('X-Goog-Resource-ID', 'empty')
            state = request.args.get('X-Goog-Resource-State', 'empty')
            resource_uri = request.args.get('X-Goog-Resource-URI', 'empty')
            goog_changed = request.args.get('X-Goog-Changed', 'empty')
            goog_chan_exp = request.args.get('X-Goog-Channel-Expiration', 'empty')
            goog_chan_token = request.args.get('X-Goog-Channel-Token', 'empty')

            print('chan_id: {}'.format(chan_id))
            print('msg_num: {}'.format(msg_num))
            print('rid: {}'.format(rid))
            print('state: {}'.format(state))
            print('resource_uri: {}'.format(resource_uri))
            print('goog_changed: {}'.format(goog_changed))
            print('goog_chan_exp: {}'.format(goog_chan_exp))
            print('goog_chan_token: {}'.format(goog_chan_token))
            print('request data ', request.get_json())
            print('requester ', str(request.args.to_dict()))


        except Exception as e:
            print('notifications() exception: {}'.format(e))

        print('leaving notifications()')

        return response('done', 200)