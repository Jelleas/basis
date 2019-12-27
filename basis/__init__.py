import sys

from basis.lang.BasisLexer import BasisLexer
from basis.lang.BasisParser import BasisParser
from basis.lang.interpreter import Interpreter

from basis.eval.stdlib import STDOUT

import basis.eval.factories.all

from antlr4 import FileStream, CommonTokenStream

__all__ = ["interpret"]

def interpret(filepath, factory = basis.eval.factories.all):
    input_stream = FileStream(filepath)
    lexer = BasisLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BasisParser(stream)
    tree = parser.start()

    program = Interpreter(factory).visit(tree)
    program.eval()

    return factory.stdlib.STDOUT.read()
