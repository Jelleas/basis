from basis.eval.factories import factory
from . import Evaluable
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
        return factory().Null()

    def __str__(self):
        return ""

class NullLiteral(Evaluable):
    def eval(self):
        return factory().Null()

    def __str__(self):
        return f"{factory().Null()}"


class IntLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return factory().Int(self.val)

    def __str__(self):
        return str(factory().Int(self.val))


class FloatLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return factory().Float(self.val)

    def __str__(self):
        return str(factory().Float(self.val))


class BoolLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return factory().Bool(self.val)

    def __str__(self):
        return str(factory().Bool(self.val))


class StringLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return factory().String(self.val)

    def __str__(self):
        return str(factory().String(self.val))


class ArrayLiteral(Evaluable):
    def __init__(self, items):
        self.items = items

    def eval(self):
        return factory().Array([item.eval() for item in self.items])

    def __str__(self):
        return str(factory().Array(self.items))
