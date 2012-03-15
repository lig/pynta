import os, unittest

from webob import Request

from pynta.conf import settings
from pynta.core.session import Session

from test_project.test_app import Application


class PyntaSessionTest(unittest.TestCase):

    def setUp(self):
        self.app = Application()
        session = Session()
        session.save()
        self.session_key = session.key

    def runTest(self):
        request = Request({})
        request.method = 'GET'
        request.headers['Cookie'] = 'PYNTA_SESSION_ID=%s' % self.session_key
        self.app.request = request
        self.app.dispatch({})
        self.assertEqual(self.app.session.key, self.session_key)

    def tearDown(self):
        os.remove(settings.STORAGE_DBM['filename'])


suite = unittest.TestSuite([PyntaSessionTest()])
