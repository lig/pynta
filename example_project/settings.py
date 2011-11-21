import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

INSTALLED_APPS = (
    ('/', 'example_app'),
    ('/media/', 'pynta.apps.simple.Static'),
)

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
