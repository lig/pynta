from webob import Request, Response
from webob.exc import HTTPServerError, HTTPNotFound, HTTPMethodNotAllowed

from pynta.conf.provider import SettingsProvider
from pynta.core.session import LazySession, Session
from pynta.core.urls import UrlMatch, url


class PyntaAppBase(SettingsProvider):

    handle_settings = 'templates', 'storage'


class PyntaApp(Response, metaclass=PyntaAppBase):
    ALLOWED_HTTP_METHODS = ('GET', 'POST', 'HEAD')

    urls = (
        (r'^$', 'self', {}, ''),
    )

    responsable = False

    def __init__(self, *args, **kwargs):
        super(PyntaApp, self).__init__(*args, **kwargs)
        self.urls = [isinstance(u, UrlMatch) and u or url(*u) for u in self.urls]

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

                    if self.responsable:
                        return self.call(environ, start_response)
                    else:
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
            action_name = params['_action']
            method = getattr(self, 'do_%s' % action_name, None)

            if method:
                # del '_action' parameter from params
                del params['_action']
            else:
                # raise server error if we have no requested method
                raise HTTPServerError()

        else:
            # fall back to choose app method according to http method
            action_name = None
            method = getattr(self, self.request.method.lower())

        # prepare context for method
        self.context = self.get_context(**params)
        # get data from method
        data = method(**params)

        # use template renderer if app has it
        if hasattr(self, 'templates'):
            self.text = str(self.templates.render(data, action_name))
        elif isinstance(data, str):
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

    def get_context(self, **kwargs):
        return {}

    def get(self, **kwargs):
        return self.context

    def post(self, **kwargs):
        return self.get(**kwargs)

    def head(self, **kwargs):
        return None
