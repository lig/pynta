from pynta.apps.generic import CRUDApp
from pynta.templates import Mako
from pynta.storage import Anydbm


class TestCRUDApp(CRUDApp):

    object_name = 'test'
    storage = Anydbm
    templates = Mako

    class templates_settings:
        template = 'test_$action.mako.html'
