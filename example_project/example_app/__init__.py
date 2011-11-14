from pynta.core import PyntaApp
from pynta.storage import Anydbm
from pynta.templates import PlainText

from hi import HiApp


class Application(PyntaApp):

    urls = (
        (r'^$', 'self', {}, 'hello'),
        (r'^(?P<host>[^:]*)', r'^hi/$', HiApp, {'name': 'pal'}, 'hi'),
        (r'^(?P<host>[^:]*)', r'^hi/(?P<name>\w+)/$', HiApp, {}, 'hi'),
    )

    class storage_settings:
        filename = 'local.db'

    def get(self):
        return 'Hello!'
