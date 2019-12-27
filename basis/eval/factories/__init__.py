import importlib

FACTORY = None

def factory():
    return FACTORY

def _import(module_name):
    """Import module and create a shallow copy"""
    mod = importlib.import_module(module_name)
    new = type(mod)(mod.__name__, mod.__doc__)
    new.__dict__.update(mod.__dict__)
    return new
