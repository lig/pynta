from pynta.core import PyntaApp
from pynta.templates import PlainText

from hi import HiApp


class Application(PlainText, PyntaApp):

    urls = (
        (r'^$', 'self', {}, 'hello'),
        (r'^(?P<host>[^:]*)', r'^hi/$', HiApp, {'name': 'pal'}, 'hi'),
        (r'^(?P<host>[^:]*)', r'^hi/(?P<name>\w+)/$', HiApp, {}, 'hi'),
    )

    def get(self):
        return 'Hello!'
