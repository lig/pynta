import pytest

from webob import Request

from fixture_project.test_app import Application
from fixture_project.test_app.plaintext_app import PlaintextApp
from fixture_project.test_app.mako_app import MakoApp
from fixture_project.test_app.jinja2_app import Jinja2App
from fixture_project.test_app.mongodb_app import MongodbApp
from fixture_project.test_app.mongoengine_app import MongoengineApp


@pytest.fixture(params=range(6))
def app_fixture(request):
    apps = [
        (Application, ''),
        (PlaintextApp, "['test output']"),
        (MakoApp, 'test output\n'),
        (Jinja2App, 'test output\n'),
        (MongodbApp, 'test output\n'),
        (MongoengineApp, 'test output\n'),
    ]
    return apps[request.param]


def test_pynta_app(app_fixture):
    app_class, etalon_output = app_fixture

    request = Request({})
    request.method = 'GET'

    app = app_class()
    app.request = request
    app.dispatch({})

    assert app.text == etalon_output
