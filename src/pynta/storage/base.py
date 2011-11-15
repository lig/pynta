import anydbm


class Storage(object):

    settings_name = ''

    class storage_settings:
        pass


class Anydbm(Storage):

    settings_name = 'STORAGE_ANYDBM'

    class storage_settings:
        filename = None
        flag = 'r'
        mode = 0666


    def __init__(self, *args, **kwargs):
        super(Anydbm, self).__init__(*args, **kwargs)
        self.db = anydbm.open(self.storage_settings.filename,
            self.storage_settings.flag, self.storage_settings.mode)


    def __del__(self):
        self.db.close()
        super(Anydbm, self).__del__()
