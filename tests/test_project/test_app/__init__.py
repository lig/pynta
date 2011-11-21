from pynta.apps import PyntaApp


class Application(PyntaApp):

    def get(self):
        return u''

    def render(self, data):
        return u'%s' % data
