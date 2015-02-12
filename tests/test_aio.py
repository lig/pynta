from io import BytesIO
import pytest

from aiohttp.multidict import CIMultiDict
from aiohttp.protocol import RawRequestMessage, HttpVersion11

from fixture_project.test_app import Application
import asyncio


class StreamWriter(BytesIO):
    def drain(self):
        return ()


@pytest.fixture(params=range(1))
def app_fixture(request):
    apps = [
        (Application, b'test text'),
    ]
    return apps[request.param]


def test_pynta_app(app_fixture):
    app_class, etalon_output = app_fixture

    message = RawRequestMessage(
        'GET', '/', HttpVersion11, CIMultiDict(), False, False)

    app = app_class()
    handler = app.make_handler()()
    handler.writer = StreamWriter()

    loop = asyncio.new_event_loop()
    loop.run_until_complete(handler.handle_request(message, ''))
    loop.close()

    assert handler.writer.getvalue().splitlines()[-1] == etalon_output
