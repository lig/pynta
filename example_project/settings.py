import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

TEMPLATES_MAKO = {
    'directories': [
        os.path.join(PROJECT_ROOT, 'templates')
    ]
}

STORAGE_ANYDBM = {
    'flag': 'n',
    'filename': 'example.db'
}

SESSION_STORAGE = 'pynta.storage.Anydbm'
