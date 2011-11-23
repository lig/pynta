from pynta.apps import PyntaApp
from pynta.templates import Mako


class ActionApp(PyntaApp):

    urls = (
        (r'^(?P<_action>(list|detail))/(?P<parameter>.*)$', 'self', {}, 'test'),
    )

    templates = Mako

    class templates_settings:
        template = 'test.mako.html'


    def _list(self, parameter):
        return {'test': u'list %s' % parameter}

    def _detail(self, parameter):
        return {'test': u'detail %s' % parameter}
