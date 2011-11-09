from base import PlainText

try:
    from makotemplates import Mako
except ImportError:
    print 'Mako templates support disabled.'
