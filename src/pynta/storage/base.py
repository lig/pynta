from pynta.conf.provider import settings_provider_factory


class StorageMixin(object):

    __metaclass__ = settings_provider_factory('storage')

    storage_settings_name = ''

    @property
    def storage(self):
        NotImplemented


class Anydbm(StorageMixin):
    storage_settings_name = 'STORAGE_ANYDBM'

    filename = None
    flag = 'r'
    mode = 0666


    def __init__(self, *args, **kwargs):
        super(Anydbm, self).__init__(*args, **kwargs)
        import anydbm
        self.db = anydbm.open(self.filename, self.flag, self.mode)


    @property
    def storage(self):
        return self.db


    def __del__(self):
        self.db.close()
        super(Anydbm, self).__del__()
