from pynta.apps import PyntaApp
from pynta.storage import Anydbm
from pynta.templates import PlainText

from hi import HiApp


class Application(PyntaApp):

    urls = (
        (r'^$', 'self', {}, 'hello'),
        (r'^(?P<host>[^:]*)', r'^hi/$', HiApp, {'name': 'pal'}, 'hi'),
        (r'^(?P<host>[^:]*)', r'^hi/(?P<name>\w+)/$', HiApp, {}, 'hi'),
    )

    templates = PlainText
    storage = Anydbm

    class storage_settings:
        filename = 'local.db'


    def get(self):
        return 'Hello!'
