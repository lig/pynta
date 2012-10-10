import shelve as dbm
from abc import ABCMeta, abstractmethod, abstractproperty
from pickle import dumps, loads
from uuid import uuid4

from pynta.conf.provider import SettingsConsumer


class Storage(SettingsConsumer):
    """
    Storage interface class. Defines typical storage properties and methods.
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def settings_name(self):
        return NotImplemented

    @abstractproperty
    class settings:
        pass

    @abstractmethod
    def get(self, tag, key):
        """
        Returns object stored under tag `tag` and key `key`.
        Think of tag like of the table or collection.
        Type of the `object` depends on storage realization.
        """
        return NotImplemented

    @abstractmethod
    def put(self, tag, key, obj):
        """
        Stores object `obj` under tag `tag` and key `key`.
        Returned value depends on storage realization.
        """
        return NotImplemented

    @abstractmethod
    def delete(self, tag, key):
        """
        Deletes object stored under tag `tag` and key `key`.
        Returned value depends on storage realization.
        """
        return NotImplemented

    @abstractmethod
    def get_free_key(self, tag):
        """
        Returns free key for tag `tag`.
        It is normal for storage to create new object for this key to prevent
        this key usage. Thus application is encouraged to use this key and do
        not throw it away if using this method.
        """
        return NotImplemented

    @abstractmethod
    def get_dataset(self, tag):
        """
        Returns dataset for tag `tag`.

        Dataset should realize dict api.
        """
        return NotImplemented


class Anydbm(Storage):

    settings_name = 'STORAGE_ANYDBM'

    class settings:
        filename = ''
        flag = 'r'
        mode = 0o666

    def __init__(self, *args, **kwargs):
        super(Anydbm, self).__init__(*args, **kwargs)
        self.db = dbm.open(self.settings.filename)

    def __del__(self):
        self.db.close()
        super(Anydbm, self).__del__()

    def get(self, tag, key):
        return loads(self.db[self._get_object_key(tag, key)])

    def put(self, tag, key, obj):
        self.db[self._get_object_key(tag, key)] = dumps(obj)

    def delete(self, tag, key):
        del self.db[self._get_object_key(tag, key)]

    def get_free_key(self, tag):
        """
        Uses `uuid.uuid4` for key generation without checking if this key is
        free really.
        """
        return uuid4().hex

    def get_dataset(self, tag):
        return [{k: loads(v)} for k, v in self.db.items() if
            k.startswith('%s+' % tag)]

    def _get_object_key(self, tag, key):
        return str('%s+%s' % (tag, key))
