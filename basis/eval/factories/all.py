import basis.eval.constructs as constructs
import basis.eval.types as types
import basis.eval.stdlib as stdlib


def init():
    import sys
    import basis.eval
    basis.eval.init(sys.modules[__name__])
