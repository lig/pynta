import re

from pynta.utils.collections import filter_dict
from pynta.utils.decorators import add_first_arg


class UrlMatch(object):

    def __init__(self, host_pattern, url_pattern, app, params, name):
        self.host_regex = host_pattern and re.compile(host_pattern)
        self.url_regex = url_pattern and re.compile(url_pattern)
        self.app = app
        self.default_params = params
        self.name = name

    def match(self, host, path):
        # we will store any match result till the next match() invocation only
        self.match_result = None

        params = dict(self.default_params) or {}

        if self.host_regex:
            host_match = self.host_regex.match(host)

            if host_match:
                params.update(filter_dict(host_match.groupdict()))
            else:
                return False

        if self.url_regex:
            url_match = self.url_regex.match(path)

            if url_match:
                params.update(filter_dict(url_match.groupdict()))
            else:
                return False

        if self.app == 'self':
            # we already have correct app url and do not need to rewrite it
            app_url = ''
        else:
            # put matched pat part into app url
            app_url = path[:url_match.end()]

        self.match_result = {
            'app_url': app_url,
            'params': params
        }
        return True

    @property
    def app_url(self):
        return self.match_result and self.match_result['app_url']

    @property
    def params(self):
        return self.match_result and self.match_result['params']


@add_first_arg(None)
def url(host_pattern, url_pattern, app, params=None, name=None):
    """
    url([host_pattern, ]url_pattern, app[, params][, name])
    """

    if isinstance(app, type):
        app = app()

    params = params or {}
    return UrlMatch(host_pattern=host_pattern, url_pattern=url_pattern,
        app=app, params=params, name=name)
