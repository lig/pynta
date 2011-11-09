from pynta.core import PyntaApp
from pynta.templates import Mako


class HiApp(Mako, PyntaApp):

    template = 'hi.html'

    def get(self, name):
        return {'name': u'%s' % name}
