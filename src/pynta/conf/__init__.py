"""
It is likely that settings module is placed in the project root directory and
main `pynta` binary is started from that directory.
"""
import os
import sys
from warnings import warn

from paste.util.import_string import import_module, try_import_module


class ConfigurationError(Exception):
    pass


class UnconfiguredSettings(object):

    def __getattribute__(self, name):
        raise ConfigurationError('Settings is not configured yet.')


class Settings(object):
    """
    Proxy for project settings module.

    Lets access project settings as `pynta.conf.settings` module.
    """
    _settings = None

    def __init__(self, settings_module_name=None):

        if settings_module_name:
            self._settings = import_module(settings_module_name)
        else:
            sys.path.insert(0, os.path.curdir)
            self._settings = try_import_module('settings')

        if not self._settings:
            warn('Cannot find settings. Using empty settings placeholder.')
            self._settings = import_module('pynta.conf.empty_settings')

        from pynta import conf
        conf.settings = self

    def __nonzero__(self):
        return bool(self._settings)

    def __getattr__(self, name):
        return getattr(self._settings, name)

    def __setattr__(self, name, value):

        if name == '_settings':

            if self._settings:
                raise ConfigurationError('Settings is already configured.')
            else:
                super(Settings, self).__setattr__(name, value)

        else:
            raise ConfigurationError('You cannot change settings at runtime.')

    def __delattr__(self, name):
        raise ConfigurationError('You cannot change settings at runtime.')


settings = UnconfiguredSettings()
