import random

from pynta.apps import PyntaApp
from pynta.templates import Mako
from pynta.storage import Mongoengine


class MongoengineApp(PyntaApp):

    templates = Mako
    storage = Mongoengine

    class templates_settings:
        template = 'test.mako.html'

    def get(self):
        random_key = random.randint(1, 10000)
        self.storage.put('test', random_key, {'test': 'test output'})
        return self.storage.get('test', random_key)
