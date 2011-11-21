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


    def __init__(self, session_key=None):
        self.key = session_key

        if self.key:
            # restoring session data from storage
            self.load()

            if not isinstance(self.data, dict):
                # possible data loss
                raise KeyError('No data for session_key "%s"' % self.key)

        else:
            # new session
            self.key = self.storage.get_free_key()
            self.data = {}
            self.save()


    def __del__(self):
        self.save()
        super(Session, self).__del__()


    def load(self):
        self.data = self.storage.get('session', self.key)
        return self.data


    def save(self):
        if self.key:
            self.storage.put('session', self.key, self.data)
        else:
            raise KeyError('No session key defined. Deleted session?')


    def delete(self):
        self.storage.delete('session', self.key)
        # prevent session saving after deleting
        self.key = None


    def __getitem__(self, name):
        return self.data[name]


    def __setitem__(self, name, value):
        self.data[name] = value


    def __delitem__(self, name):
        del self.data[name]


class LazySession(object):
    """
    Session wrapper that will not access session storage until session data
    will be accessed.
    """

    real_session_class = Session
    trigger_method_names = ('load', 'delete', '__getitem__', '__setitem__',
        '__delitem__')

    def __init__(self, session_key=None):
        self.key = session_key

    def __getattr__(self, name):

        if name in self.trigger_method_names:
            self.__class__ = self.real_session_class
            self.__init__(self.key)
            return getattr(self, name)
        else:
            return self.do_nothing()

    def do_nothing(self, *args, **kwargs):
        pass
