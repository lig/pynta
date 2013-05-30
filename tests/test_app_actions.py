import os

import pytest

from pynta.conf import settings

from fixture_project.test_app.action_app import ActionApp
from fixture_project.test_app.crud_app import TestCRUDApp


@pytest.fixture(params=range(2))
def action_app_fixture(request):
    apps = [
        (ActionApp, '/list/test', 'list test\n'),
        (ActionApp, '/detail/test', 'detail test\n'),
    ]
    return apps[request.param]


@pytest.fixture(params=range(2))
def crud_app_fixture(request):
    apps = [
        (TestCRUDApp, '/', "[{'test+2': 'test2'}, {'test+1': 'test1'}]\n"),
        (TestCRUDApp, '/1', 'test1\n'),
    ]
    return apps[request.param]


def test_pynta_action_app(action_app_fixture):
    app_class, path_info, etalon_output = action_app_fixture

    app = app_class()

    app(
        {'SERVER_NAME': 'test', 'SERVER_PORT': 80,
            'PATH_INFO': path_info, 'REQUEST_METHOD': 'GET'},
        lambda status, headers: None)

    assert app.text == etalon_output


def test_pynta_crud_app(crud_app_fixture):
    app_class, path_info, etalon_output = crud_app_fixture

    app = app_class()

    app.storage.put('test', 1, 'test1')
    app.storage.put('test', 2, 'test2')

    app(
        {'SERVER_NAME': 'test', 'SERVER_PORT': 80,
            'PATH_INFO': path_info, 'REQUEST_METHOD': 'GET'},
        lambda status, headers: None)

    assert app.text == etalon_output

    db_path = settings.STORAGE_ANYDBM['filename']
    if os.path.exists(db_path):
        os.remove(db_path)
