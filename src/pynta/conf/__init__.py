import os, sys

from paste.util.import_string import try_import_module


sys.path.insert(0, os.path.curdir)

settings = try_import_module('settings')

if not settings:
    print >> sys.stderr, 'No settings. Are you in the project dir?'
    sys.exit(1)
