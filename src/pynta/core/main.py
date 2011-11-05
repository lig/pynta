from paste.urlmap import URLMap
from paste.util.import_string import try_import_module

from pynta.conf import settings


class Pynta(URLMap):

    def __init__(self):
        URLMap.__init__(self)

        for url, app_name in settings.INSTALLED_APPS:
            app_package = try_import_module(app_name)
            self[url] = app_package.App(settings)
