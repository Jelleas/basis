from . import Evaluable
from basis.data import *
import basis.logger as logger


__all__ = ["Assignment", "Block", "Function", "FunctionCall", "Sequence", "Variable"]


class UndefinedVariable(Exception):
    pass

class FunctionError(Exception):
    pass


class Stack:
    def __init__(self):
        self.frames = []

    def push(self, frame):
        self.frames.append(frame)

    def pop(self):
        return self.frames.pop()

    def __setitem__(self, variable_name, val):
        for frame in self.frames[::-1]:
            if variable_name in frame:
                frame[variable_name] = val
                break
        else:
            self.frames[-1][variable_name] = val


    def __getitem__(self, variable):
        for frame in self.frames[::-1]:
            if variable in frame:
                return frame[variable]
        raise UndefinedVariable(f"variable '{variable}' is undefined")


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
            STACK[str(self.variable)] = result
            log(logger.emphasize(f"{self.variable} = {result}"))


    def __str__(self):
        return f"{self.variable} = {self.val}"


class Sequence(Evaluable):
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        for statement in self.statements:
            result = statement.eval()
        return result

    def __str__(self):
        return ", ".join(str(stat) for stat in self.statements)


class Block(Sequence):
    def eval(self):
        STACK.push(Frame())
        try:
            return super().eval()
        finally:
            STACK.pop()

    def __str__(self):
        return "\n".join(str(stat) for stat in self.statements)


class Function(Evaluable):
    def __init__(self, name, var_list, code):
        self.name = name
        self.variables = var_list
        self.code = code

    def eval(self):
        with logger.context("Func Def") as log:
            log(f"function {self.name}({', '.join(str(v) for v in self.variables)})")
            STACK[str(self.name)] = self


class FunctionCall(Evaluable):
    def __init__(self, name, arg_list):
        self.name = name
        self.arguments = arg_list

    def eval(self):
        with logger.context("Func Call") as log:
            log(f"{self.name}({', '.join(str(a) for a in self.arguments)})")

            # Grab the function from the stack
            function = STACK[str(self.name)]

            # Assert arg count
            if len(function.variables) != len(self.arguments):
                start = "Too few" if len(function.variables) > len(self.arguments) else "Too many"
                raise FunctionError(
                    f"{start} arguments passed for function {self.name}, "
                    f"expected {len(function.variables)}, but got {len(self.arguments)}"
                )

            # Create a new Frame for this function call
            frame = Frame()
            STACK.push(frame)
            try:
                # Create all new variables on that frame
                for var, arg in zip(function.variables, self.arguments):
                    frame[str(var)] = arg.eval()

                # Execute the function
                return function.code.eval()
            finally:
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
