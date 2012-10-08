from pickle import dumps, loads

from pymongo.connection import Connection
from pynta.storage.base import Storage


class Mongodb(Storage):

    settings_name = 'STORAGE_MONGODB'

    class settings:
        host = 'localhost'
        port = 27017
        max_pool_size = 10
        network_timeout = None
        document_class = dict
        tz_aware = False
        database = 'test'

    def __init__(self, *args, **kwargs):
        super(Mongodb, self).__init__(*args, **kwargs)
        self.connection = Connection(host=self.settings.host,
            port=self.settings.port,
            max_pool_size=self.settings.max_pool_size,
            network_timeout=self.settings.network_timeout,
            document_class=self.settings.document_class,
            tz_aware=self.settings.tz_aware)
        self.db = self.connection[self.settings.database]

    def __del__(self):
        self.connection.disconnect()
        super(Mongodb, self).__del__()

    def get(self, tag, key):
        stored_obj = self.db[tag].find_one(key)

        if stored_obj:

            if '_obj' in stored_obj:
                obj = loads(stored_obj['_obj'])
            else:
                obj = stored_obj
                del obj['_id']

        else:
            obj = stored_obj

        return obj

    def put(self, tag, key, obj):

        if isinstance(obj, dict):
            obj_to_save = obj
            obj_to_save['_id'] = key
        else:
            obj_to_save = {}
            obj_to_save['_id'] = key
            obj_to_save['_obj'] = dumps(obj)

        self.db[tag].save(obj_to_save)

    def delete(self, tag, key):
        self.db[tag].remove(key)

    def get_free_key(self, tag):
        return self.db[tag].save({})

    def get_dataset(self, tag):
        return self.db[tag].find()
