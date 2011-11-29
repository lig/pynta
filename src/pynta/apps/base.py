from webob import Request, Response
from webob.exc import HTTPServerError, HTTPNotFound, HTTPMethodNotAllowed

from pynta.conf.provider import SettingsProvider
from pynta.core.session import LazySession, Session
from pynta.core.urls import UrlMatch


class PyntaAppBase(SettingsProvider):

    handle_settings = 'templates', 'storage'


class PyntaApp(Response):

    __metaclass__ = PyntaAppBase

    ALLOWED_HTTP_METHODS = ('GET', 'POST', 'HEAD')

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

                if self.request.method in self.ALLOWED_HTTP_METHODS:
                    self.dispatch(params)
                    return Response.__call__(self, environ, start_response)
                else:
                    return HTTPMethodNotAllowed()(environ, start_response)

            else:
                environ['SCRIPT_NAME'] += url_match.app_url
                environ['PATH_INFO'] = self.request.path_info.lstrip('/')[len(
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

            if method:
                # del '_action' parameter from params
                del params['_action']
            else:
                # raise server error if we have no requested method
                raise HTTPServerError()

        else:
            # fall back to choose app method according to http method
            method = getattr(self, self.request.method.lower())

        # get data from method
        data = method(**params)

        # use template renderer if app has it
        if hasattr(self, 'templates'):
            self.text = unicode(self.templates.render(data))
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


    @staticmethod
    def require_method(*method_names):

        def decorator(func):

            def wrapper(self, **kwargs):

                if self.request.method in method_names:
                    return func(self, **kwargs)

                else:
                    raise HTTPMethodNotAllowed()

            return wrapper

        return decorator


    @staticmethod
    def action(func):

        def wrapper(self, **kwargs):
            self.params = kwargs
            self.context = self.get_context()
            result = func(self, **kwargs)

            if isinstance(result, dict):
                self.context.update(result)
                return self.context

            else:
                return result

        return wrapper


    def get_context(self):
        return self.params


    @PyntaApp.action
    def get(self, **kwargs):
        return {}


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
