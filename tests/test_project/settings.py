import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATES_MAKO = {
    'directories': [
        os.path.join(PROJECT_ROOT, 'templates')
    ]
}

TEMPLATES_CHEETAH = {
    'template_dir': os.path.join(PROJECT_ROOT, 'templates')
}

STORAGE_ANYDBM = {
    'flag': 'n',
    'filename': 'test.db'
}

SESSION_STORAGE = 'pynta.storage.Anydbm'
