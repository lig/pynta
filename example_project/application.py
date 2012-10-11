from pynta.apps import PyntaApp
from pynta.apps.simple import Static
from pynta.core.urls import url

from example_app import Application as ExampleApplication


class Application(PyntaApp):
    urls = (
        url(r'^media/', Static),
        url(r'^', ExampleApplication),
    )
