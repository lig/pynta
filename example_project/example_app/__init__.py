from pynta.core import PyntaApp

from hi import HiApp


class Application(PyntaApp):

    urls = (
        (r'^$', 'self', {}, 'hello'),
        (r'^hi/$', HiApp, {'name': 'pal'}, 'hi'),
        (r'^hi/(?P<name>\w+)/$', HiApp, {}, 'hi'),
    )

    def get(self):
        return 'Hello!'
