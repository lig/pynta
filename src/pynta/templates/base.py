class Renderer(object):

    settings_name = ''

    class settings:
        pass

    def render(self, data):
        return NotImplemented


class PlainText(Renderer):

    settings_name = 'TEMPLATES_PLAINTEXT'

    def render(self, data):
        return u'%s' % data
