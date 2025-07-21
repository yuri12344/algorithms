import socket
from collections import namedtuple
from io import BytesIO
import ipdb
# Import necessary classes and exceptions from server module
from server import ProtocolHandler, Error, CommandError, Server

class Client(object):
    def __init__(self, host='127.0.0.1', port=31337):
        self._protocol = ProtocolHandler()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((host, port))
        self._fh = self._socket.makefile('rwb')

    def execute(self, *args):
        self._protocol.write_response(self._fh, args)
        resp = self._protocol.handle_request(self._fh)
        if isinstance(resp, Error):
            raise CommandError(resp.message)
        return resp

    def get(self, key):
        return self.execute('GET', key)

    def set(self, key, value):
        return self.execute('SET', key, value)

    def delete(self, key):
        return self.execute('DELETE', key)

    def flush(self):
        return self.execute('FLUSH')

    def mget(self, *keys):
        return self.execute('MGET', *keys)

    def mset(self, *items):
        if len(items) % 2 != 0:
            raise CommandError('MSET requires an even number of arguments')
        return self.execute('MSET', *items)


if __name__ == '__main__':
    client = Client()
    ipdb.set_trace()
