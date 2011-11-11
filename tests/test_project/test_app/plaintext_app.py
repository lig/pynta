from pynta.core import PyntaApp
from pynta.templates import PlainText


class PlaintextApp(PlainText, PyntaApp):

    def get(self):
        return ['test output']
