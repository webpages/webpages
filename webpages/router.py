import os
from .tools import import_module


class Router(object):
    """
    Allow to match url address with appropriate controller.
    """
    def __init__(self, project_dir=os.getcwd()):
        self._routes = {}
        self._project_dir = project_dir
        self.load_routes()

    def load_routes(self):
        """
        Load all routes in project's folder 'controllers'.

        Ignore files with leading underscore (for example: controllers/_blog.py)
        """
        for file_name in os.listdir(os.path.join(self._project_dir, 'controllers')):
            # ignore disabled controllers
            if not file_name.startswith('_'):
                module_name = file_name.split('.', 1)[0]
                module_path = "controllers.{}".format(module_name)
                module = import_module(module_path)
                controllers = [getattr(module, x) for x in dir(module) if x != 'Controller' and x.endswith('Controller')]
                controller = controllers[0]
                self._routes[module_name] = controller
        return self._routes

    def add_route(self, path, controller):
        """Add new path and appropriate request handler (controller)."""
        self._routes[path] = controller

    def get_controller(self, path):
        """
        Return controller that handle given path.

        Args:
         - path: requested path, like: /blog/post_view/15
        """
        path_info = path.lstrip('/').split('/', 2)
        try:
            return self._routes.get(path_info[0] + '/' + path_info[1])
        except (IndexError, KeyError):
            return self._routes.get(path_info[0] or 'index')
