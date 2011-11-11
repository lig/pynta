from pynta.core import PyntaApp
from pynta.templates import Mako


class MakoApp(Mako, PyntaApp):

    template = 'test.mako.html'

    def get(self):
        return {'test': 'test output'}
