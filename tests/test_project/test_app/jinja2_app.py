from pynta.apps import PyntaApp
from pynta.templates import Jinja2


class Jinja2App(PyntaApp):

    templates = Jinja2

    class templates_settings:
        template = 'test.jinja2.html'

    def get(self):
        return {'test': 'test output'}
