import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

INSTALLED_APPS = (
    ('/', 'example_app'),
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
