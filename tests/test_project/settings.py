import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATES_MAKO = {
    'directories': [
        os.path.join(PROJECT_ROOT, 'templates')
    ]
}

STORAGE_DBM = {
    'flag': 'c',
    'filename': 'test.db'
}

SESSION_STORAGE = 'pynta.storage.Dbm'
