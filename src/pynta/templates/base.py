from abc import ABCMeta, abstractmethod, abstractproperty

from pynta.conf.provider import SettingsConsumer


class Renderer(SettingsConsumer, metaclass=ABCMeta):
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
        return '%s' % data
