from pynta.apps import PyntaApp
from pynta.apps.simple import Static

from example_app import Application as ExampleApplication


class Application(PyntaApp):
    urls = (
        (r'^media/', Static, {}, 'hi'),
        (r'^', ExampleApplication, {}, ''),
    )
