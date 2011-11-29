class Renderer(object):

    settings_name = ''

    class settings:
        pass

    def render(self, data, action=None):
        return NotImplemented


class PlainText(Renderer):

    settings_name = 'TEMPLATES_PLAINTEXT'

    def render(self, data, action=None):
        return u'%s' % data
