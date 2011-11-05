from webob import Request, Response


class BasePyntaApp(type):
    pass


class PyntaApp(Response):

    __metaclass__ = BasePyntaApp


    def __init__(self, settings, *args, **kwargs):
        super(PyntaApp, self).__init__(*args, **kwargs)
        self.settings = settings


    def __call__(self, environ, start_response):
        self.request = Request(environ)
        self.environ = environ
        self.body = self.get_body()
        return super(PyntaApp, self).__call__(environ, start_response)


    def get_body(self):
        return NotImplemented
