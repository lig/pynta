from pynta.apps import PyntaApp
from pynta.templates import PlainText


class Bug22App(PyntaApp):

    urls = (
        (r'^(?P<host>[^:]*)', r'^(?P<name>\w+)?$', 'self', {'name': 'pal'},
            'test'),
    )

    templates = PlainText

    def get_context(self, name, host):
        return {'name': u'%s' % name, 'host': u'%s' % host}
