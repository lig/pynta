from pynta.core import PyntaApp
from pynta.templates import Mako


class MakoApp(PyntaApp):

    templates = Mako

    class templates_settings:
        template = 'test.mako.html'

    def get(self):
        return {'test': 'test output'}
