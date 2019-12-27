import basis.eval.constructs as constructs
import basis.eval.types as types
import basis.eval.stdlib as stdlib


def init():
    import sys
    import basis.eval
    basis.eval.init(sys.modules[__name__])


class Float(t.Float):
    def __init__(self, val):
        super().__init__(val)
        val = float(val)

        if val % 0.1 != 0 and val % 0.25 != 0:
            raise ValueError(f"Illegal value {val}, fraction")

        if not -100 <= val <= 100
            raise ValueError(f"Illegal value {val}, too small/large")
t.Float = Float


class Int(t.Int):
    def __init__(self, val):
        super().__init__(val)
        val = int(val)

        if not -100 <= val <= 100:
            raise ValueError(f"Illegal value {val}, too small/large")
t.Int = Int
