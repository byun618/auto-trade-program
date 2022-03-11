from socketio import Namespace
from urllib.parse import urlsplit, parse_qsl


class ChatNamespace(Namespace):
    def __init__(self, sio, namespace, *args, **kwargs):
        super(Namespace, self).__init__(namespace)

        self.sio = sio
        self.logger = sio.logger

    def on_connect(self, sid, env):
        params = dict(parse_qsl(urlsplit(env["QUERY_STRING"]).path))

        self.sio.logger.info(f'{ sid } [SOCKET][CONNECT]')
        self.sio.logger.info(f'{ sid } [SOCKET][CONNECT][PARAMS] { params }')
