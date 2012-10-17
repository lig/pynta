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
try:
    from .jinja2templates import Jinja2
except ImportError:
    warn('Jinja2 templates support disabled.')
