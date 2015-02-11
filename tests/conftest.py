import os
import sys


def pytest_configure(config):

    try:
        from pynta.conf import setup_settings
    except ImportError:
        # No pynta on PYTHONPATH. May be we are in the source dir?
        src_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
            os.pardir))
        if os.path.exists(src_path):
            # Let's import from there then.
            sys.path.insert(0, src_path)
            from pynta.conf import setup_settings

    setup_settings('fixture_project.settings')
