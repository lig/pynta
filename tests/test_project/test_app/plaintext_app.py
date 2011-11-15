from pynta.core import PyntaApp
from pynta.templates import PlainText


class PlaintextApp(PyntaApp):

    templates = PlainText

    def get(self):
        return ['test output']
