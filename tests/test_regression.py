"""
github#22: Pynta shares data across serial requests
"""

from fixture_project.test_app.bug22_app import Bug22App


def test_bug22():

    def start_response(*args, **kwargs):
        pass

    app = Bug22App()

    environ1 = {
        'SERVER_NAME': 'localhost',
        'SERVER_PORT': 8000,
        'PATH_INFO': '/',
        'REQUEST_METHOD': 'GET',
    }
    environ2 = {
        'SERVER_NAME': 'localhost',
        'SERVER_PORT': 8000,
        'PATH_INFO': '/user',
        'REQUEST_METHOD': 'GET',
    }
    environ3 = environ1

    app(environ1, start_response)
    app(environ2, start_response)
    app(environ3, start_response)

    assert app.text == "OrderedDict([('name', 'pal'), ('host', 'localhost')])"
