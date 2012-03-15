from pynta.apps.generic import CRUDApp
from pynta.templates import Mako
from pynta.storage import Dbm


class TestCRUDApp(CRUDApp):

    object_name = 'test'
    storage = Dbm
    templates = Mako

    class templates_settings:
        template = 'test_$action.mako.html'
