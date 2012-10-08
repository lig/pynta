from pynta.apps import PyntaApp
from pynta.templates import Mako


class HiApp(PyntaApp):

    templates = Mako

    class templates_settings:
        template = 'hi.html'


    def get_context(self, name, host):
        return {'name': '%s' % name, 'host': '%s' % host}
