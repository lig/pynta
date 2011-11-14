from pynta.core import PyntaApp
from pynta.templates import Mako


class HiApp(PyntaApp):

    templates = Mako

    template = 'hi.html'

    def get(self, name, host):
        return {'name': u'%s' % name, 'host': u'%s' % host}
