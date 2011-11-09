import os, sys

from paste.util.import_string import try_import_module


class ConfigurationError(Exception):
    pass


sys.path.insert(0, os.path.curdir)
settings = try_import_module('settings')

if not settings:
    raise ConfigurationError('No settings. Are you in the project dir?')
