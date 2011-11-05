import os, sys

from paste.urlmap import URLMap
from paste.util.import_string import try_import_module
from webob import Request, Response


class BasePyntaApp(type):
    pass


class Pynta(URLMap):
    
    def __init__(self):
        URLMap.__init__(self)
        
        sys.path.insert(0, os.path.curdir)
        
        settings = try_import_module('settings')
        
        if not settings:
            print >> sys.stderr, 'No settings. Are you in the project dir?'
            sys.exit(1)
        
        for url, app_name in settings.INSTALLED_APPS:
            app_package = try_import_module(app_name)
            self[url] = app_package.App()


class PyntaApp(Response):
    
    __metaclass__ = BasePyntaApp
    
    
    def __call__(self, environ, start_response):
        self.request = Request(environ)
        self.environ = environ
        self.body = self.get_body()
        return super(PyntaApp, self).__call__(environ, start_response)
    
    
    def get_body(self):
        return NotImplemented
