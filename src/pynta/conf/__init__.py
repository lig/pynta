"""
It is likely that settings module is placed in the project root directory and
main `pynta` binary is started from that directory.
"""
import os
import sys
from importlib import import_module
from warnings import warn


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

    def __init__(self, settings_module):
        self._settings = settings_module
        from pynta import conf
        conf.settings = self

    def __bool__(self):
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


def setup_settings(settings_module_name=None):

    if settings_module_name:
        settings_module = import_module(settings_module_name)
    else:
        sys.path.insert(0, os.path.curdir)
        settings_module = import_module('settings')

    if not settings_module:
        warn('Cannot find settings. Using empty settings placeholder.')
        settings_module = import_module('pynta.conf.empty_settings')

    Settings(settings_module)
