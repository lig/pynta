from pynta.apps import PyntaApp
from pynta.storage import Anydbm
from pynta.templates import PlainText

from .hi import HiApp


class Application(PyntaApp):

    urls = (
        (r'^$', 'self', {}, 'hello'),
        (r'^(?P<host>[^:]*)', r'^hi/(?P<name>\w+)?$', HiApp, {'name': 'pal'},
            'hi'),
    )

    templates = PlainText
    storage = Anydbm

    class storage_settings:
        filename = 'local.db'


    def get(self):
        return 'Hello!'
