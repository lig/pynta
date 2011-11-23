from webob import Request, Response
from webob.exc import HTTPServerError, HTTPNotFound

from pynta.conf.provider import SettingsProvider
from pynta.core.session import LazySession, Session
from pynta.core.urls import UrlMatch

ALLOWED_HTTP_METHODS = ('GET', 'POST', 'HEAD')


class PyntaAppBase(SettingsProvider):

    handle_settings = 'templates', 'storage'


class PyntaApp(Response):

    __metaclass__ = PyntaAppBase

    urls = (
        (r'^$', 'self', {}, ''),
    )

    def __init__(self, *args, **kwargs):
        super(PyntaApp, self).__init__(*args, **kwargs)

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
                    self.dispatch(params)
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


    def dispatch(self, params):
        # init session
        self.init_session()

        # check for action
        if '_action' in params:
            # choose app method by action name
            method = getattr(self, '_%s' % params['_action'], None)

            if not method:
                # raise server error if we have no requested method
                raise HTTPServerError()

        else:
            # fall back to choose app method according to http method
            method = getattr(self, self.request.method.lower())

        # get data from method
        data = method(**params)

        # use template renderer if app has it
        if hasattr(self, 'templates'):
            self.text = self.templates.render(data)
        elif isinstance(data, unicode):
            self.text = data

        # save session
        self.save_session()


    def init_session(self):
        session_key = self.request.cookies.get('PYNTA_SESSION_ID')
        self.session = LazySession(session_key)


    def save_session(self):

        if isinstance(self.session, Session):

            if self.session.key:
                self.set_cookie('PYNTA_SESSION_ID', self.session.key)
            else:
                self.delete_cookie('PYNTA_SESSION_ID')


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


    def _url(self, host_pattern, url_pattern, app_class, params, name):

        if app_class == 'self':
            app = 'self'
        else:
            app = app_class()

        return UrlMatch(host_pattern=host_pattern, url_pattern=url_pattern,
            app=app, params=params, name=name)
