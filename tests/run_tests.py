#!/usr/bin/env python
import os, sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import unittest

from pynta.conf import Settings
Settings('test_project.settings')

from base import suite as base_suite
from session import suite as session_suite
from app_actions import suite as app_actions_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite([base_suite, session_suite, app_actions_suite])
    runner.run(suite)
