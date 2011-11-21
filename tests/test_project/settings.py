import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATES_MAKO = {
    'directories': [
        os.path.join(PROJECT_ROOT, 'templates')
    ]
}

SESSION_STORAGE = 'pynta.storage.Mongodb'
