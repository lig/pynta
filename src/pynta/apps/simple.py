import os

from webob.static import FileApp

from pynta.apps import PyntaApp
from pynta.conf import settings


class Static(PyntaApp):

    urls = (
        (r'^(?P<filename>.+)$', 'self', {}, 'static'),
    )

    responsable = True

    def get(self, filename):
        self.file_app = FileApp(os.path.join(settings.MEDIA_ROOT, filename))

    def call(self, environ, start_response):
        return self.file_app(environ, start_response)
