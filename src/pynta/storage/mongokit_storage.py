from mongokit.connection import Connection
from pynta.storage.mongodb import Mongodb


class Mongokit(Mongodb):
    """
    @todo: implement full storage interface using mongokit
    """

    settings_name = 'STORAGE_MONGOKIT'

    def __init__(self, *args, **kwargs):
        self.connection = Connection(host=self.settings.host,
            port=self.settings.port,
            max_pool_size=self.settings.max_pool_size,
            network_timeout=self.settings.network_timeout,
            document_class=self.settings.document_class,
            tz_aware=self.settings.tz_aware)
        self.db = self.connection[self.settings.database]
        object.__init__(self, *args, **kwargs)
