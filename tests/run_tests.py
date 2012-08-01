#!/usr/bin/env python
import os
import sys

import unittest

try:
    from pynta.conf import Settings
except ImportError:
    # No pynta on PYTHONPATH. May be we are in the source dir?
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        os.pardir, 'src'))
    if os.path.exists(src_path):
        # Let's import from there then.
        sys.path.insert(0, src_path)
        from pynta.conf import Settings

Settings('test_project.settings')

from base import suite as base_suite
from session import suite as session_suite
from app_actions import suite as app_actions_suite
from regression import suite as regression_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite(
        [base_suite, session_suite, app_actions_suite, regression_suite])
    runner.run(suite)
