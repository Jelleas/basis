from . import _import
constructs = _import("basis.eval.constructs")
types = _import("basis.eval.types")
stdlib = _import("basis.eval.stdlib")


def init():
    import sys
    import basis.eval
    basis.eval.init(sys.modules[__name__])


class IllegalValueError(Exception):
    pass


class Float(types.Float):
    def __init__(self, val):
        super().__init__(val)
        val = float(val)

        if val % 0.1 != 0 and val % 0.25 != 0:
            raise IllegalValueError(f"Illegal value {val}, fraction")

        if not -100 <= val <= 100:
            raise IllegalValueError(f"Illegal value {val}, too small/large")
types.Float = Float


class Int(types.Int):
    def __init__(self, val):
        super().__init__(val)
        val = int(val)

        if not -100 <= val <= 100:
            raise IllegalValueError(f"Illegal value {val}, too small/large")
types.Int = Int
