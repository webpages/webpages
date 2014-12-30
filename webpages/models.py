from .tools import import_module


class Model(object):

    @property
    def app_name(self):
        return self.__class__.__module__.__name__

    def get_global_id(self):
        return "{}/{}#{}".format(self.app_name, self.__class__.__name__, self.id)

    @staticmethod
    def get_object_by_global_id(global_id):
        """
        Find object by GlobalID and return appropriate model instance.
        """
        app_name, tail = global_id.split('/', 1)
        model_name, object_id = tail.split('#', 1)
        path_to_controller = "{}/controllers/{}".format(app_name, model_name.lower())
        model = import_module(path_to_controller)
        return model.get_object_by_id(object_id)
