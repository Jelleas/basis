from basis.eval.factories import factory
from basis.eval.carriers import Evaluable
import basis.logger as logger

__all__ = ["NoOp",
           "NullLiteral",
           "IntLiteral",
           "FloatLiteral",
           "BoolLiteral",
           "StringLiteral",
           "ArrayLiteral"]

class NoOp(Evaluable):
    def eval(self):
        return factory().types.Null()

    def __str__(self):
        return ""

class NullLiteral(Evaluable):
    def eval(self):
        return factory().types.Null()

    def __str__(self):
        return f"{factory().types.Null()}"


class IntLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return factory().types.Int(self.val)

    def __str__(self):
        return str(factory().types.Int(self.val))


class FloatLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return factory().types.Float(self.val)

    def __str__(self):
        return str(factory().types.Float(self.val))


class BoolLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return factory().types.Bool(self.val)

    def __str__(self):
        return str(factory().types.Bool(self.val))


class StringLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return factory().types.String(self.val)

    def __str__(self):
        return str(factory().types.String(self.val))


class ArrayLiteral(Evaluable):
    def __init__(self, items):
        self.items = items

    def eval(self):
        return factory().types.Array([item.eval() for item in self.items])

    def __str__(self):
        return str(factory().types.Array(self.items))
