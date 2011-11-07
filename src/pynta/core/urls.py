import re


class UrlMatch(object):

    def __init__(self, host_pattern, url_pattern, app, params, name):
        self.host_regex = host_pattern and re.compile(host_pattern)
        self.url_regex = url_pattern and re.compile(url_pattern)
        self.app = app
        self.default_params = params
        self.name = name


    def match(self, host, path):
        params = self.default_params or {}

        if self.host_regex:
            host_match = self.host_regex.match(host)

            if host_match:
                params.update(host_match.groupdict())
            else:
                return False

        if self.url_regex:
            url_match = self.url_regex.match(path)

            if url_match:
                params.update(url_match.groupdict())
            else:
                return False

        self.app_url = path[:url_match.end()]
        self.params = params
        return True
