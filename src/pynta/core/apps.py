from webob import Request, Response
from webob.exc import HTTPServerError, HTTPNotFound

from urls import UrlMatch


ALLOWED_HTTP_METHODS = ('GET', 'POST', 'HEAD')


class BasePyntaApp(type):
    pass


class PyntaApp(Response):

    __metaclass__ = BasePyntaApp

    urls = (
        (r'^$', 'self', {}, ''),
    )


    def __init__(self, settings, *args, **kwargs):
        super(PyntaApp, self).__init__(*args, **kwargs)
        self.settings = settings

        urls = []
        for url in self.urls:

            if len(url) == 4:
                url = (None,) + url

            urls.append(self._url(*url))

        self.urls = urls


    def __call__(self, environ, start_response):
        self.request = Request(environ)
        self.environ = environ

        url_match = self.app_by_url()

        if url_match:
            params = self.environ.get('params', {})
            params.update(url_match.params)

            if url_match.app == 'self':

                if self.request.method in ALLOWED_HTTP_METHODS:
                    method = getattr(self, self.request.method.lower())
                    self.body = self.render(method(**params))
                    return Response.__call__(self, environ, start_response)
                else:
                    return HTTPServerError(
                        'Method %s is not allowed on this server' %
                            self.request.method)(environ, start_response)

            else:
                environ['SCRIPT_NAME'] += url_match.app_url
                environ['PATH_INFO'] = self.request.path_info[len(
                    url_match.app_url):]
                environ['params'] = params
                return url_match.app(environ, start_response)

        else:
            return HTTPNotFound('%s is not found on this server' %
                self.request.path)(environ, start_response)


    def app_by_url(self):
        host = self.request.host
        path = self.request.path_info.lstrip('/')

        for url_match in self.urls:
            if url_match.match(host, path):
                return url_match


    def get(self, **kwargs):
        return kwargs


    def post(self, **kwargs):
        return self.get(**kwargs)


    def head(self, **kwargs):
        return None


    def render(self, context):
        if context is not None:
            return '%s' % context


    def _url(self, host_pattern, url_pattern, app_class, params, name):

        if app_class == 'self':
            app = 'self'
        else:
            app = app_class(self.settings)

        return UrlMatch(host_pattern=host_pattern, url_pattern=url_pattern,
            app=app, params=params, name=name)
