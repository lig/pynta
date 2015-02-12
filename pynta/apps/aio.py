from aiohttp.web import Application, Response

from pynta.conf.provider import SettingsProvider


class PyntaAppBase(SettingsProvider):

    handle_settings = 'templates', 'storage'


class PyntaApp(Application, metaclass=PyntaAppBase):

    def __init__(self, *args, **kwargs):
        Application.__init__(self, *args, **kwargs)
        self.router.add_route('GET', '/', self.dispatch)

    def dispatch(self, request):
        return Response(text='')
