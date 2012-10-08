#!/usr/bin/env python3

from argparse import ArgumentParser
from importlib import import_module

from pynta.conf import Settings
from pynta.core.server import serve

argument_parser = ArgumentParser()
argument_parser.add_argument('--settings', default=None,
    help='Settings module name')


def get_main_app():
    return import_module('application').Application()


def main():
    params = argument_parser.parse_args()
    Settings(params.settings)
    # @todo: handle host, port and app in params
    serve('localhost', 8000, get_main_app())


if __name__ == '__main__':
    main()
