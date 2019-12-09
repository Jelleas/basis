from . import Evaluable
from basis.data import *
import basis.logger as logger


__all__ = ["Assignment",
           "PreIncrementAssignment",
           "PreDecrementAssignment",
           "PostIncrementAssignment",
           "PostDecrementAssignment",
           "Block",
           "Function",
           "FunctionCall",
           "Return",
           "Sequence",
           "Variable"]


class UndefinedVariable(Exception):
    pass

class FunctionError(Exception):
    pass

class ReturnSignal(Exception):
    def __init__(self, payload):
        super().__init__(self)
        self.payload = payload


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
            log(str(self))
            result = self.val.eval()
            STACK[str(self.variable)] = result
            log(logger.emphasize(f"{self.variable} = {result}"))


    def __str__(self):
        return f"{self.variable} = {self.val}"


class PreIncrementAssignment(Evaluable):
    def __init__(self, variable):
        self.variable = variable

    def eval(self):
        with logger.context("PRE INCREMENT") as log:
            log(str(self))
            val = self.variable.eval().add(Int(1))
            STACK[str(self.variable)] = val
            return val

    def __str__(self):
        return f"++{self.variable}"


class PreDecrementAssignment(Evaluable):
    def __init__(self, variable):
        self.variable = variable

    def eval(self):
        with logger.context("PRE DECREMENT") as log:
            log(str(self))
            val = self.variable.eval().sub(Int(1))
            STACK[str(self.variable)] = val
            return val

    def __str__(self):
        return f"--{self.variable}"


class PostIncrementAssignment(Evaluable):
    def __init__(self, variable):
        self.variable = variable

    def eval(self):
        with logger.context("POST INCREMENT") as log:
            log(str(self))
            val = self.variable.eval()
            STACK[str(self.variable)] = val.add(Int(1))
            return val

    def __str__(self):
        return f"{self.variable}++"


class PostDecrementAssignment(Evaluable):
    def __init__(self, variable):
        self.variable = variable

    def eval(self):
        with logger.context("POST DECREMENT") as log:
            log(str(self))
            val = self.variable.eval()
            STACK[str(self.variable)] = val.sub(Int(1))
            return val

    def __str__(self):
        return f"{self.variable}--"


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
        with logger.context("FUNC DEF") as log:
            log(f"function {self.name}({', '.join(str(v) for v in self.variables)})")
            STACK[str(self.name)] = self


class FunctionCall(Evaluable):
    def __init__(self, name, arg_list):
        self.name = name
        self.arguments = arg_list

    def eval(self):
        with logger.context("FUNC CALL") as log:
            log(str(self))

            # Grab the function from the stack
            function = STACK[str(self.name)]

            # Assert arg count
            if len(function.variables) != len(self.arguments):
                start = "Too few" if len(function.variables) > len(self.arguments) else "Too many"
                raise FunctionError(
                    f"{start} arguments passed for function {self.name}, "
                    f"expected {len(function.variables)}, but got {len(self.arguments)}"
                )

            # Eval all args
            args = [arg.eval() for arg in self.arguments]

            # Create a new Frame for this function call
            frame = Frame()
            STACK.push(frame)
            try:
                # Create all new variables on that frame
                for var, arg in zip(function.variables, args):
                    frame[str(var)] = arg

                # Execute the function
                try:
                    function.code.eval()
                except ReturnSignal as r:
                    result = r.payload
                else:
                    result = Null()

                log(f"{self} => {logger.emphasize(result)}")
                return result
            finally:
                STACK.pop()

    def __str__(self):
        return f"{self.name}({', '.join(str(a) for a in self.arguments)})"


class Return(Evaluable):
    def __init__(self, code):
        self.code = code

    def eval(self):
        with logger.context("RETURN") as log:
            log(str(self))
            raise ReturnSignal(self.code.eval())

    def __str__(self):
        return f"return {self.code}"


class Variable(Evaluable):
    def __init__(self, variable):
        self.variable = variable

    def eval(self):
        with logger.context("VAR EXP") as log:
            result = STACK[str(self.variable)]
            log(f"{str(self.variable)} => {logger.emphasize(str(result))}")
            return result

    def __str__(self):
        return self.variable
