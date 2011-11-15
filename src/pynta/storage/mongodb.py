from pymongo.connection import Connection
from pynta.storage.base import Storage


class Mongodb(Storage):

    settings_name = 'STORAGE_MONGODB'

    class storage_settings:
        host = 'localhost'
        port = 27017
        max_pool_size = 10
        network_timeout = None
        document_class = dict
        tz_aware = False
        database = 'test'


    def __init__(self, *args, **kwargs):
        self.connection = Connection(host=self.storage_settings.host,
            port=self.storage_settings.port,
            max_pool_size=self.storage_settings.max_pool_size,
            network_timeout=self.storage_settings.network_timeout,
            document_class=self.storage_settings.document_class,
            tz_aware=self.storage_settings.tz_aware)
        self.db = self.connection[self.storage_settings.database]
        super(Mongodb, self).__init__(*args, **kwargs)

    def __del__(self):
        self.connection.disconnect()
        super(Mongodb, self).__del__()
