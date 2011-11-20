from paste.urlmap import URLMap
from paste.util.import_string import simple_import

from pynta.conf import settings


class Pynta(URLMap):

    def __init__(self):
        URLMap.__init__(self)

        for url, app_name in settings.INSTALLED_APPS:
            app = simple_import(app_name)

            if hasattr(app, 'Application'):
                app_class = app.Application
            else:
                app_class = app

            if app_class:
                # @todo: allow use of any wsgi app
                self[url] = app_class()
            else:
                print ('Ignoring %s from INSTALLED_APPS setting: cannot find '
                    'app class.' % app_name)
