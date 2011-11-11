from pynta.conf.provider import settings_provider_factory


class RendererMixin(object):

    __metaclass__ = settings_provider_factory('renderer')

    renderer_settings_name = ''

    def render(self, data):
        return NotImplemented


class PlainText(RendererMixin):

    renderer_settings_name = 'TEMPLATES_PLAINTEXT'

    def render(self, data):
        return u'%s' % data
