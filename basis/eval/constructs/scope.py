from . import Evaluable, Assignable
from basis.eval.types import *
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
           "Variable",
           "Index"]


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
        self.frames = [Frame()]

    def push(self, frame):
        self.frames.append(frame)

    def pop(self):
        return self.frames.pop()

    def __setitem__(self, variable_name, val):
        for frame in self.frames[::-1]:
            if variable_name in frame:
                frame[variable_name] = val
                return
            if isinstance(frame, BlockingFrame):
                break

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


class BlockingFrame(Frame):
    """Blocks assignment in any previous frames."""
    pass


STACK = Stack()


class Assignment(Evaluable):
    def __init__(self, assignable, val):
        self.assignable = assignable
        self.val = val

    def eval(self):
        with logger.context("ASSIGNMENT") as log:
            log(str(self))
            result = self.val.eval()
            self.assignable.assign(result)
            log(logger.emphasize(f"{self.assignable} = {result}"))

    def __str__(self):
        return f"{self.assignable} = {self.val}"


class PreIncrementAssignment(Evaluable):
    def __init__(self, assignable):
        self.assignable = assignable

    def eval(self):
        with logger.context("PRE INCREMENT") as log:
            log(str(self))
            val = self.assignable.eval().add(Int(1))
            self.assignable.assign(val)
            return val

    def __str__(self):
        return f"++{self.assignable}"


class PreDecrementAssignment(Evaluable):
    def __init__(self, assignable):
        self.assignable = assignable

    def eval(self):
        with logger.context("PRE DECREMENT") as log:
            log(str(self))
            val = self.assignable.eval().sub(Int(1))
            self.assignable.assign(val)
            return val

    def __str__(self):
        return f"--{self.assignable}"


class PostIncrementAssignment(Evaluable):
    def __init__(self, assignable):
        self.assignable = assignable

    def eval(self):
        with logger.context("POST INCREMENT") as log:
            log(str(self))
            val = self.assignable.eval()
            self.assignable.assign(val.add(Int(1)))
            return val

    def __str__(self):
        return f"{self.assignable}++"


class PostDecrementAssignment(Evaluable):
    def __init__(self, assignable):
        self.assignable = assignable

    def eval(self):
        with logger.context("POST DECREMENT") as log:
            log(str(self))
            val = self.assignable.eval()
            self.assignable.assign(val.sub(Int(1)))
            return val

    def __str__(self):
        return f"{self.assignable}--"


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
            log(str(self))
            STACK[str(self.name)] = self

    def __str__(self):
        return f"function {self.name}({', '.join(str(v) for v in self.variables)})"


class FunctionCall(Evaluable):
    def __init__(self, atom, arg_list):
        self.atom = atom
        self.arguments = arg_list

    def eval(self):
        with logger.context("FUNC CALL") as log:
            log(str(self))

            # Grab the function
            function = self.atom.eval()

            # Assert arg count
            if len(function.variables) != len(self.arguments):
                start = "Too few" if len(function.variables) > len(self.arguments) else "Too many"
                raise FunctionError(
                    f"{start} arguments passed for function {self.atom}, "
                    f"expected {len(function.variables)}, but got {len(self.arguments)}"
                )

            # Eval all args
            args = [arg.eval() for arg in self.arguments]

            # Create a new BlockingFrame for this function call
            STACK.push(BlockingFrame())
            try:
                # Create all new variables on that frame

                for var, arg in zip(function.variables, args):
                    var.assign(arg)

                # Execute the function
                try:
                    function.code.eval()
                except ReturnSignal as r:
                    result = r.payload
                else:
                    result = Null()

                log(f"{self._format(function.name, args)} => {logger.emphasize(result)}")
                return result
            finally:
                STACK.pop()

    def __str__(self):
        return self._format(self.atom, self.arguments)

    def _format(self, name, arguments):
        return f"{name}({', '.join(str(a) for a in arguments)})"


class Return(Evaluable):
    def __init__(self, code):
        self.code = code

    def eval(self):
        with logger.context("RETURN") as log:
            log(str(self))
            raise ReturnSignal(self.code.eval())

    def __str__(self):
        return f"return {self.code}"


class Variable(Assignable):
    def __init__(self, variable):
        self.variable = variable

    def eval(self):
        with logger.context("VAR EXP") as log:
            result = STACK[str(self.variable)]
            log(f"{str(self.variable)} => {logger.emphasize(str(result))}")
            return result

    def assign(self, val):
        STACK[str(self)] = val

    def __str__(self):
        return self.variable


class Index(Assignable):
    def __init__(self, iterable, index):
        self.iterable = iterable
        self.index = index
        self._cached_iterable = None
        self._cached_index = None

    def eval(self):
        with logger.context("INDEX") as log:
            log(str(self))
            iterable = self.iterable.eval()
            self._cached_iterable = iterable
            index = self.index.eval()
            self._cached_index = index
            result = iterable.index(index)
            log(f"{iterable}[{index}] => {logger.emphasize(result)}")
            return result

    def assign(self, val):
        iterable = self._cached_iterable
        if iterable is None:
            iterable = self.iterable.eval()

        index = self._cached_index
        if index is None:
            index = self.index.eval()

        iterable.index_assign(index, val)

    def __str__(self):
        return f"{self.iterable}[{self.index}]"
