from . import constructs
from . import types
from . import stdlib

__all__ = []

# load stdlib
for name, val in stdlib.export.items():
    constructs.scope.STACK[name] = val
