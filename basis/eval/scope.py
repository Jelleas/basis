from . import Evaluable
from basis.data import *
import basis.logger as logger


__all__ = ["Assignment", "Block", "Variable"]


class Stack:
    def __init__(self):
        self.frames = []

    def push(self, frame):
        self.frames.append(frame)

    def pop(self):
        return self.frames.pop()

    def __getitem__(self, variable):
        for frame in self.frames[::-1]:
            if variable in frame:
                return frame[variable]


class Frame:
    def __init__(self):
        self._variable_map = {}

    def __setitem__(self, variable_name, val):
        self._variable_map[variable_name] = val

    def __getitem__(self, variable_name):
        return self._variable_map[variable_name]

    def __contains__(self, variable_name):
        return variable_name in self._variable_map


STACK = Stack()


class Assignment(Evaluable):
    def __init__(self, variable, val):
        self.variable = variable
        self.val = val

    def eval(self):
        with logger.context("ASSIGNMENT") as log:
            log(f"{self.variable} = {self.val}")
            result = self.val.eval()
            STACK.frames[-1][str(self.variable)] = result
            log(logger.emphasize(f"{self.variable} = {result}"))


class Block(Evaluable):
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        STACK.push(Frame())
        for statement in self.statements:
            statement.eval()
        STACK.pop()


class Variable(Evaluable):
    def __init__(self, variable):
        self.variable = variable

    def eval(self):
        with logger.context("Var Exp") as log:
            log(str(self.variable))
            result = STACK[str(self.variable)]
            log(logger.emphasize(str(result)))
            return result

    def __str__(self):
        return self.variable
