from warnings import warn

from base import Anydbm
try:
    from mongodb import Mongodb
except ImportError:
    warn('Mongodb storage support disabled.')
try:
    from mongokit_storage import Mongokit
except ImportError:
    warn('Mongokit storage support disabled.')
