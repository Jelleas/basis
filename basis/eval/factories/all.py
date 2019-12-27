from . import _import
constructs = _import("basis.eval.constructs")
types = _import("basis.eval.types")
stdlib = _import("basis.eval.stdlib")


def init():
    import sys
    import basis.eval
    basis.eval.init(sys.modules[__name__])
