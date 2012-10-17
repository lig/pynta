import unittest

from webob import Request

from test_project.test_app import Application
from test_project.test_app.plaintext_app import PlaintextApp
from test_project.test_app.mako_app import MakoApp
from test_project.test_app.cheetah_app import CheetahApp
from test_project.test_app.mongodb_app import MongodbApp
from test_project.test_app.mongoengine_app import MongoengineApp


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
    PyntaAppTest(app_class=CheetahApp, etalon_output='test output\n'),
    PyntaAppTest(app_class=MongodbApp, etalon_output='test output\n'),
    PyntaAppTest(app_class=MongoengineApp, etalon_output='test output\n'),
])
