from argparse import ArgumentParser

from paste import httpserver
from paste import reloader

from conf import Settings
from core import Pynta

argument_parser = ArgumentParser()
argument_parser.add_argument('--settings', default=None,
    help='Settings module name')
argument_parser.add_argument('--reload', action='store_true', default=False)


def main():
    # prepare command line arguments
    params = argument_parser.parse_args()
    
    # install reloader if requested
    if params.reload:
        reloader.install()
    
    # init settings and serve Pynta
    Settings(params.settings)
    httpserver.serve(Pynta())


if __name__ == '__main__':
    main()
