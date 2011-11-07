from pynta.core import PyntaApp


class HiApp(PyntaApp):

    def get(self, name):
        return 'Hi %s!' % name
