from paste.util.import_string import simple_import

from pynta.conf import settings
from pynta.conf.provider import SettingsProvider


class SessionBase(SettingsProvider):

    handle_settings = ('storage',)

    def __new__(cls, name, bases, args):
        storage_name = settings.SESSION_STORAGE
        storage_class = simple_import(storage_name)
        args.update({'storage': storage_class})
        return SettingsProvider.__new__(cls, name, bases, args)


class Session(object):

    __metaclass__ = SessionBase
