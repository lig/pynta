import os
import string

from jinja2 import Environment, FileSystemLoader

from pynta.conf import settings

from .base import Renderer


class Jinja2(Renderer):

    settings_name = 'TEMPLATES_JINJA2'

    class settings:
        searchpath = None
        template = None

    def __init__(self, *args, **kwargs):
        super(Jinja2, self).__init__(*args, **kwargs)
        self.environment = Environment(
            loader=FileSystemLoader(self.settings.searchpath or
                os.path.join(settings.PROJECT_ROOT, 'templates')))

    def render(self, data, action_name=None):

        if action_name and '$action' in self.settings.template:
            template_name = string.Template(self.settings.template).substitute(
                action=action_name)
        else:
            template_name = self.settings.template

        return self.environment.get_template(template_name).render(**data)
