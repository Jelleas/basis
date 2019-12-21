from . import Evaluable
from basis.data import *
import basis.logger as logger


class NullLiteral(Evaluable):
    def eval(self):
        return Null()

    def __str__(self):
        return f"{Null()}"


class IntLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Int(self.val)

    def __str__(self):
        return str(Int(self.val))


class FloatLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Float(self.val)

    def __str__(self):
        return str(Float(self.val))


class BoolLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Bool(self.val)

    def __str__(self):
        return str(Bool(self.val))


class StringLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return String(self.val)

    def __str__(self):
        return str(String(self.val))


class ArrayLiteral(Evaluable):
    def __init__(self, items):
        self.items = items

    def eval(self):
        return Array([item.eval() for item in self.items])

    def __str__(self):
        return str(Array(self.items))
