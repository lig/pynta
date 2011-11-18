import os, mimetypes

from pynta.conf import settings
from pynta.core import PyntaApp


class Static(PyntaApp):

    urls = (
        (r'^(?P<filename>.*)$', 'self', {}, 'static'),
    )

    def get(self, filename):
        """
        @todo: use technique described at 
            http://docs.webob.org/en/latest/file-example.html
        """
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        self.content_type = mimetypes.guess_type(filepath)[0]
        self.body_file = open(filepath)
