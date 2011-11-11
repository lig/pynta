import os, sys

from paste.util.import_string import import_module


class ConfigurationError(Exception):
    pass


class UnconfiguredSettings(object):

    def __getattribute__(self, name):
        raise ConfigurationError('Settings is not configured yet.')


class Settings(object):

    _settings = None


    def __init__(self, settings_module_name=None):
        from pynta import conf

        if settings_module_name:
            self._settings = import_module(settings_module_name)
        else:
            sys.path.insert(0, os.path.curdir)
            self._settings = import_module('settings')

        conf.settings = self


    def __nonzero__(self):
        return bool(self._settings)


    def __getattr__(self, name):
        return getattr(self._settings, name)


    def __setattr__(self, name, value):

        if name == '_settings':

            if self._settings:
                raise NotImplementedError('Settings is already configured.')
            else:
                super(Settings, self).__setattr__(name, value)

        else:
            raise NotImplementedError('You cannot change settings at runtime.')


    def __delattr__(self, name):
        raise NotImplementedError('You cannot change settings at runtime.')


settings = UnconfiguredSettings()
