from pynta.conf import settings
from pynta.conf.provider import SettingsProvider
from pynta.utils.importing import simple_import


class SessionBase(SettingsProvider):

    handle_settings = ('storage',)

    def __new__(cls, name, bases, args):
        storage_name = settings.SESSION_STORAGE
        storage_class = simple_import(storage_name)
        args.update({'storage': storage_class})
        return SettingsProvider.__new__(cls, name, bases, args)


class Session(object, metaclass=SessionBase):
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
            self.key = self.storage.get_free_key('session')
            self.data = {}
            self.save()

    def __del__(self):
        self.save()

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

    def __init__(self, session_key=None):
        self.key = session_key

    def save(self):
        pass

    def _accessed(self, method_name, args=[], kwargs={}):
        self.__class__ = self.real_session_class
        self.__init__(self.key)
        return getattr(self, method_name)(*args, **kwargs)

    def load(self):
        return self._accessed('load')

    def delete(self):
        return self._accessed('delete')

    def __getitem__(self, name):
        return self._accessed('__getitem__', [name])

    def __setitem__(self, name, value):
        return self._accessed('__setitem__', [name, value])

    def __delitem__(self, name):
        return self._accessed('__delitem__', [name])
