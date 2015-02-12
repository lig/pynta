from aiohttp.web import Response

from pynta.apps.aio import PyntaApp


class Application(PyntaApp):

    def dispatch(self, request):
        return Response(text='test text')
