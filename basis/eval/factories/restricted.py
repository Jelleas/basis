from basis.eval.constructs import *
from basis.eval.stdlib import *
from basis.eval.types import *

from basis.eval.types import Float as _EvalFloat
from basis.eval.types import Int as _EvalInt

def init():
    import sys
    import basis.eval
    basis.eval.init(sys.modules[__name__])


class Float(_EvalFloat):
    def __init__(self, val):
        super().__init__(val)
        val = float(val)

        if val % 0.1 != 0 and val % 0.25 != 0:
            raise ValueError(f"Illegal value {val}, fraction")

        if not -100 <= val <= 100
            raise ValueError(f"Illegal value {val}, too small/large")


class Int(_EvalInt):
    def __init__(self, val):
        super().__init__(val)
        val = int(val)

        if not -100 <= val <= 100:
            raise ValueError(f"Illegal value {val}, too small/large")
