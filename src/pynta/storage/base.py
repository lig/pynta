class Storage(object):

    settings_name = ''

    class storage_settings:
        pass

    @property
    def storage(self):
        NotImplemented


class Anydbm(Storage):

    settings_name = 'STORAGE_ANYDBM'

    class storage_settings:
        filename = None
        flag = 'r'
        mode = 0666


    def __init__(self, *args, **kwargs):
        super(Anydbm, self).__init__(*args, **kwargs)
        import anydbm
        self._db = anydbm.open(self.storage_settings.filename,
            self.storage_settings.flag, self.storage_settings.mode)


    @property
    def storage(self):
        return self._db


    def __del__(self):
        self._db.close()
        super(Anydbm, self).__del__()
