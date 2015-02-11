import os
import string

from Cheetah.Template import Template

from pynta.conf import settings

from .base import Renderer


class Cheetah(Renderer):

    settings_name = 'TEMPLATES_CHEETAH'

    class settings:
        template_dir = None
        template = None

    def __init__(self, *args, **kwargs):
        super(Cheetah, self).__init__(*args, **kwargs)
        self.template_dir = (self.settings.template_dir or
            os.path.join(settings.PROJECT_ROOT, 'templates'))

    def render(self, data, action_name=None):
        template_name = os.path.join(self.template_dir, self.settings.template)

        if action_name and '$action' in template_name:
            template_name = string.Template(template_name).substitute(
                action=action_name)

        template = Template(file=template_name, searchList=[data])

        return str(template)
