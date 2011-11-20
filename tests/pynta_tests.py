#!/usr/bin/env python
import os, sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import unittest

from webob import Request

from pynta.conf import Settings
settings = Settings('test_project.settings')

from test_project.test_app import Application
from test_project.test_app.plaintext_app import PlaintextApp
from test_project.test_app.mako_app import MakoApp
from test_project.test_app.mongodb_app import MongodbApp


class PyntaAppTest(unittest.TestCase):

    def __init__(self, app_class, etalon_output, *args, **kwargs):
        self.app_class = app_class
        self.etalon_output = etalon_output
        super(PyntaAppTest, self).__init__(*args, **kwargs)

    def setUp(self):
        self.app = self.app_class()

    def runTest(self):
        request = Request({})
        request.method = 'GET'
        self.app.request = request
        self.app.dispatch({})
        self.assertMultiLineEqual(self.app.text, self.etalon_output)


suite = unittest.TestSuite([
    PyntaAppTest(app_class=Application, etalon_output=''),
    PyntaAppTest(app_class=PlaintextApp, etalon_output="['test output']"),
    PyntaAppTest(app_class=MakoApp, etalon_output='test output\n'),
    PyntaAppTest(app_class=MongodbApp, etalon_output='test output\n'),
])


if __name__ == '__main__':
    runner = unittest.runner.TextTestRunner()
    runner.run(suite)
