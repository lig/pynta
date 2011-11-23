import unittest

from test_project.test_app.action_app import ActionApp


class PyntaActionTest(unittest.TestCase):

    def __init__(self, path_info, etalon_output, *args, **kwargs):
        self.path_info = path_info
        self.etalon_output = etalon_output
        super(PyntaActionTest, self).__init__(*args, **kwargs)

    def runTest(self):
        app = ActionApp()
        app(
            {'SERVER_NAME': 'test', 'SERVER_PORT': 80,
                'PATH_INFO': self.path_info, 'REQUEST_METHOD': 'GET'},
            lambda status, headers: None)
        self.assertMultiLineEqual(app.text, self.etalon_output)


suite = unittest.TestSuite([
    PyntaActionTest(path_info='/list/test', etalon_output='list test\n'),
    PyntaActionTest(path_info='/detail/test', etalon_output='detail test\n'),
])
