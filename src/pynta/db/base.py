from pynta.conf.provider import settings_provider_factory


class StorageMixin(object):

    __metaclass__ = settings_provider_factory('storage')

    storage_settings_name = ''
