from basis.eval.constructs import Evaluable
from basis.eval.constructs.scope import Function, Variable, ReturnSignal


class BuiltIn(Function):
    def __init__(self):
        self.name = self.__class__.name
        self.variables = self.__class__.variables
        self.code = self.Code()


class Print(BuiltIn):
    name = "print"
    variables = [Variable("printable")]

    class Code(Evaluable):
        def eval(self):
            print(Print.variables[0].eval())


class Length(BuiltIn):
    name = "length"
    variables = [Variable("iterable")]

    class Code(Evaluable):
        def eval(self):
            length = Length.variables[0].eval().length()
            raise ReturnSignal(length)


class ToInt(BuiltIn):
    name = "int"
    variables = [Variable("value")]

    class Code(Evaluable):
        def eval(self):
            result = ToInt.variables[0].eval().to_int()
            raise ReturnSignal(result)


class ToFloat(BuiltIn):
    name = "float"
    variables = [Variable("value")]

    class Code(Evaluable):
        def eval(self):
            result = ToFloat.variables[0].eval().to_float()
            raise ReturnSignal(result)


export = {
    Print.name: Print(),
    Length.name: Length(),
    ToInt.name: ToInt(),
    ToFloat.name: ToFloat()
}
