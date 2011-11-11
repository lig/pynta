from pynta.conf.provider import SettingsProvider


class RendererMixin(object):

    __metaclass__ = SettingsProvider

    settings_name = ''

    def render(self, data):
        return NotImplemented


class PlainText(RendererMixin):

    settings_name = 'TEMPLATES_PLAINTEXT'

    def render(self, data):
        return u'%s' % data
