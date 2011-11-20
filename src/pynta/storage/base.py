import anydbm


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


class Anydbm(Storage):

    settings_name = 'STORAGE_ANYDBM'

    class settings:
        filename = None
        flag = 'r'
        mode = 0666


    def __init__(self, *args, **kwargs):
        super(Anydbm, self).__init__(*args, **kwargs)
        self.db = anydbm.open(self.settings.filename, self.settings.flag,
            self.settings.mode)


    def __del__(self):
        self.db.close()
        super(Anydbm, self).__del__()


    def get(self, tag, key):
        return self.db[self._get_object_key(tag, key)]


    def put(self, tag, key, obj):
        self.db[self._get_object_key(tag, key)] = obj


    def delete(self, tag, key):
        del self.db[self._get_object_key(tag, key)]


    def _get_object_key(self, tag, key):
        return '%s+%s' % (tag, key)
