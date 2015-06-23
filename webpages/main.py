from wsgiref.simple_server import make_server
from webob import Request, Response


class WebPages(object):
    """
    Main class to work with WebPages application.
    """

    def __init__(self):
        pass

    def run(self, host=None, port=None):
        server = make_server('127.0.0.1', 8080, app)
        server.serve_forever()
