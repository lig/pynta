from pynta.apps import PyntaApp


class Application(PyntaApp):

    def get(self):
        self.session['test'] = 'value'
        return ''

    def render(self, data):
        return '%s' % data
