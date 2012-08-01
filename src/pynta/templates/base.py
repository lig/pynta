from abc import ABCMeta, abstractmethod, abstractproperty


class Renderer(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def settings_name(self):
        return NotImplemented

    @abstractproperty
    class settings:
        pass

    @abstractmethod
    def render(self, data, action=None):
        return NotImplemented


class PlainText(Renderer):

    settings_name = 'TEMPLATES_PLAINTEXT'

    class settings:
        pass

    def render(self, data, action=None):
        return u'%s' % data
