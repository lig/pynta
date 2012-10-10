from pynta.apps import PyntaApp
from pynta.templates import Mako


class ActionApp(PyntaApp):

    urls = (
        (r'^(?P<_action>(list|detail))/(?P<parameter>.*)$',
            'self', {}, 'test'),
    )

    templates = Mako

    class templates_settings:
        template = 'test.mako.html'

    def do_list(self, parameter):
        return {'test': 'list %s' % parameter}

    def do_detail(self, parameter):
        return {'test': 'detail %s' % parameter}
