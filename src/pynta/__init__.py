from argparse import ArgumentParser

from paste import httpserver
from paste import reloader

# settings must be set before any pynta package processing
from conf import Settings
settings = Settings()

from core import Pynta

argument_parser = ArgumentParser()
argument_parser.add_argument('--reload', action='store_true', default=False)


def main():
    params = argument_parser.parse_args()
    
    if params.reload:
        reloader.install()
    
    httpserver.serve(Pynta())


if __name__ == '__main__':
    main()
