from importlib import import_module


def simple_import(name):

    if '.' not in name:
        raise ImportError(name)

    module_name, object_name = name.rsplit('.', 1)
    module = import_module(module_name)
    return getattr(module, object_name)
