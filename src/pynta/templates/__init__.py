from warnings import warn

from base import PlainText
try:
    from makotemplates import Mako
except ImportError:
    warn('Mako templates support disabled.')
