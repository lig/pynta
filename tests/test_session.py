from webob import Request

from pynta.core.session import Session

from fixture_project.test_app import Application


def test_pynta_session():
    app = Application()

    session = Session()
    session.save()
    session_key = session.key

    request = Request({})
    request.method = 'GET'
    request.headers['Cookie'] = 'PYNTA_SESSION_ID=%s' % session_key

    app.request = request
    app.dispatch({})

    assert app.session.key == session_key
