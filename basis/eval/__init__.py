__all__ = []

def init(factory):
    from . import factories
    factories.FACTORY = factory

    # load stdlib
    from . import constructs
    from . import stdlib
    for name, val in factory.export.items():
        factory.scope.STACK[name] = val
