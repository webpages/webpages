import json
from copy import deepcopy


class Settings(object):
    """
    Load project settings and become interface to
    access this settings.

    Settings are inherited from apps and redefined
    in project settings.
    """

    def __init__(self):
        raise Exception('Settings should be used via Settings.get() without instantiate it')

    @classmethod
    def __get_instance(cls):
        if not hasattr(cls, '__instance'):
            # load app configs and project config and merge them in one
            cls.__instance = json()
        return cls.__instance

    @classmethod
    def get(cls, option, default_value=None):
        """
        Return value of given option.

        If option isn't found - return default_value (None by default).

        Args:
        - option: string with path to option with `:` separator
        """
        config = cls.__get_instance()
        for name in option.split(':'):
            if not name:
                raise Exception('Incorrect value in path (maybe double `:` or empty path)')
            if name not in config:
                return default_value
            config = config[name]
        return deepcopy(config)
