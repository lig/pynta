from warnings import warn

from .base import Anydbm
try:
    from .mongodb import Mongodb
except ImportError:
    warn('Mongodb storage support disabled.')
try:
    from .mongoengine_storage import Mongoengine
except ImportError:
    warn('Mongoengine storage support disabled.')
