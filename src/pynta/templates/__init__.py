from warnings import warn

from .base import PlainText
try:
    from .makotemplates import Mako
except ImportError:
    warn('Mako templates support disabled.')
try:
    from .cheetahtemplates import Cheetah
except ImportError:
    warn('Cheetah templates support disabled.')
