from pynta.apps import PyntaApp


class Application(PyntaApp):

    def get(self):
        self.session['test'] = 'value'
        return u''

    def render(self, data):
        return u'%s' % data
