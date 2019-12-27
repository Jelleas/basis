__all__ = []

def init(factory):
    from . import factories
    factories.FACTORY = factory

    # load stdlib
    from . import constructs
    from . import stdlib
    for name, val in factory.stdlib.export.items():
        factory.constructs.scope.STACK[name] = val
