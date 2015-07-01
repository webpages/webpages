from wsgiref.simple_server import make_server
from webob import Request, Response
from .router import Router


class WebPages(object):
    """
    Main class to work with WebPages application.
    """

    def __init__(self):
        # init the router
        self._router = Router()

    def run(self, host=None, port=None):
        from wsgiref.simple_server import demo_app
        server = make_server('127.0.0.1', 8000, demo_app)
        server.serve_forever()
