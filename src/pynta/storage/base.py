import dbm
from pickle import dumps, loads
from uuid import uuid4


class Storage(object):
    """
    Storage interface class. Defines typical storage properties and methods.
    """
    settings_name = ''

    class settings:
        pass

    def get(self, tag, key):
        """
        Returns object stored under tag `tag` and key `key`.
        Think of tag like of the table or collection.
        Type of the `object` depends on storage realization. 
        """
        return NotImplemented

    def put(self, tag, key, obj):
        """
        Stores object `obj` under tag `tag` and key `key`.
        Returned value depends on storage realization.
        """
        return NotImplemented

    def delete(self, tag, key):
        """
        Deletes object stored under tag `tag` and key `key`.
        Returned value depends on storage realization.
        """
        return NotImplemented

    def get_free_key(self, tag):
        """
        Returns free key for tag `tag`.
        It is normal for storage to create new object for this key to prevent
        this key usage. Thus application is encouraged to use this key and do
        not throw it away if using this method.

        Default implementation uses `uuid.uuid4` for key generation without
        checking if this key is free really.
        """
        return uuid4().hex

    def get_dataset(self, tag):
        """
        Returns dataset for tag `tag`.
        
        Dataset should realize dict api.
        """
        return NotImplemented


class Anydbm(Storage):

    settings_name = 'STORAGE_ANYDBM'

    class settings:
        filename = None
        flag = 'r'
        mode = 666


    def __init__(self, *args, **kwargs):
        super(Anydbm, self).__init__(*args, **kwargs)
        self.db = dbm.open(self.settings.filename, self.settings.flag,
            self.settings.mode)


    def __del__(self):
        self.db.close()
        super(Anydbm, self).__del__()


    def get(self, tag, key):
        return loads(self.db[self._get_object_key(tag, key)])


    def put(self, tag, key, obj):
        self.db[self._get_object_key(tag, key)] = dumps(obj)


    def delete(self, tag, key):
        del self.db[self._get_object_key(tag, key)]


    def get_dataset(self, tag):
        return [{k: loads(v)} for k, v in self.db.items() if
            k.startswith('%s+' % tag)]


    def _get_object_key(self, tag, key):
        return str('%s+%s' % (tag, key))
