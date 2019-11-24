from . import Evaluable
from basis.data import *
import basis.logger as logger


class IntLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Int(self.val)

    def __str__(self):
        return f"{self.val}"


class FloatLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Float(self.val)

    def __str__(self):
        return f"{self.val}"


class BoolLiteral(Evaluable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Bool(self.val)

    def __str__(self):
        return f"{self.val}"
