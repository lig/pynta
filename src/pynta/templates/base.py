from pynta.conf import settings, ConfigurationError


class RendererBase(type):

    def __new__(cls, name, bases, args):
        renderer_settings_name = 'RENDERER_%s' % name.upper()
        renderer_settings = getattr(settings, renderer_settings_name, None)

        if renderer_settings:

            if not isinstance(renderer_settings, dict):
                raise ConfigurationError('%s setting must be dict.' %
                    renderer_settings_name)

            args.update(renderer_settings)

        return type.__new__(cls, name, bases, args)


class Renderer(object):

    __metaclass__ = RendererBase

    def render(self, data):
        return NotImplemented


class PlainText(Renderer):

    def render(self, data):
        return u'%s' % data
