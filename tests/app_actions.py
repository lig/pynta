import os
import unittest

from pynta.conf import settings

from test_project.test_app.action_app import ActionApp
from test_project.test_app.crud_app import TestCRUDApp


class PyntaActionTest(unittest.TestCase):

    def __init__(self, app, path_info, etalon_output, *args, **kwargs):
        self.app = app()
        self.path_info = path_info
        self.etalon_output = etalon_output
        super(PyntaActionTest, self).__init__(*args, **kwargs)

    def setUp(self):
        if hasattr(self.app, 'storage'):
            self.app.storage.put('test', 1, 'test1')
            self.app.storage.put('test', 2, 'test2')

    def runTest(self):
        self.app(
            {'SERVER_NAME': 'test', 'SERVER_PORT': 80,
                'PATH_INFO': self.path_info, 'REQUEST_METHOD': 'GET'},
            lambda status, headers: None)
        self.assertMultiLineEqual(self.app.text, self.etalon_output)

    def tearDown(self):
        if hasattr(self.app, 'storage'):
            db_path = settings.STORAGE_ANYDBM['filename']
            if os.path.exists(db_path):
                os.remove(db_path)


suite = unittest.TestSuite([
    PyntaActionTest(app=ActionApp, path_info='/list/test',
        etalon_output='list test\n'),
    PyntaActionTest(app=ActionApp, path_info='/detail/test',
        etalon_output='detail test\n'),
    PyntaActionTest(app=TestCRUDApp, path_info='/',
        etalon_output="[{'test+2': 'test2'}, {'test+1': 'test1'}]\n"),
    PyntaActionTest(app=TestCRUDApp, path_info='/1', etalon_output='test1\n'),
])
