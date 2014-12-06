from .core import Settings


class ProjectController(object):

    def not_found(self, request):
        """
        Page not found in all apps.
        """
        return 'Not found'


def get_controler(app_name, controller_name):
    return None


def handle_request(request):
    # each request comes via all middlewares

    # prevent change original request
    requested_url = request.url

    # show static content (for empy path or None we don't handle static)
    static_dir = Settings.get('project:files:static_dir')
    if static_dir and requested_url.startswith(static_dir + '/'):
        return "content of static file: {}".format(requested_url)

    # detect home page (empty url)
    if requested_url in ('', '/'):
        requested_url = Settings.get('project:homepage')

    # run page controller
    path_info = request.url.split('/', 3)
    app_name = path_info[0]
    controller_name = len(path_info) > 1 and path_info[1] or None
    method_name = len(path_info) > 2 and path_info[2] or None
    if method_name in ('', '/'):
        method_name = 'index'
    # 1. controller don't found
    if not app_name or not controller_name:
        return getattr(ProjectController, 'not_found')(request)
    # 2. run controller's method
    controller = get_controler(app_name, controller_name)
    if hasattr(controller, method_name):
        return getattr(controller, method_name)(request)
    # 3. run controller's not_found method
    elif hasattr(controller, 'not_found'):
        return getattr(controller, 'not_found')(request)
    # 4. run global not_found method
    else:
        return getattr(ProjectController, 'not_found')(request)
