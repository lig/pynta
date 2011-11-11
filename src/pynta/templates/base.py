class RendererMixinBase(type):

    def __new__(cls, name, bases, args):
        from pynta.conf import settings

        renderer_settings_name = args.get('renderer_settings_name')

        if renderer_settings_name:
            # Base I'm. Just project settings I need.
            renderer_settings = getattr(settings, renderer_settings_name, {})
        else:
            # find base settings name 
            renderer_bases = filter(
                lambda base: hasattr(base, 'renderer_settings_name'),
                bases)

            if renderer_bases:
                # we have settings
                renderer_settings_name = getattr(renderer_bases[0],
                    'renderer_settings_name')
                renderer_settings = getattr(settings, renderer_settings_name,
                    {})
                # update renderer_settings with my args
                renderer_settings.update(args)
            else:
                renderer_settings = {}

        # update args with calculated settings
        args.update(renderer_settings)

        return type.__new__(cls, name, bases, args)


class RendererMixin(object):

    __metaclass__ = RendererMixinBase

    renderer_settings_name = ''

    def render(self, data):
        return NotImplemented


class PlainText(RendererMixin):

    renderer_settings_name = 'TEMPLATES_PLAINTEXT'

    def render(self, data):
        return u'%s' % data
