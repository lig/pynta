from pynta.apps import PyntaApp
from pynta.templates import Cheetah


class CheetahApp(PyntaApp):

    templates = Cheetah

    class templates_settings:
        template = 'test.cheetah.html'

    def get(self):
        return {'test': 'test output'}
