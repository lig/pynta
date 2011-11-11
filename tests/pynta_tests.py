import unittest

from pynta.conf import Settings
settings = Settings('test_project.settings')

from test_project.test_app import Application
from test_project.test_app.plaintext_app import PlaintextApp
from test_project.test_app.mako_app import MakoApp


class PyntaAppTest(unittest.TestCase):

    app_class = Application
    etalon_output = ''

    def setUp(self):
        self.app = self.app_class(settings)

    def runTest(self):
        output = self.app.render(self.app.get())
        self.assertMultiLineEqual(output, self.etalon_output)


class Test001PlaintextApp(PyntaAppTest):

    app_class = PlaintextApp
    etalon_output = "['test output']"


class Test002MakoApp(PyntaAppTest):

    app_class = MakoApp
    etalon_output = 'test output\n'
