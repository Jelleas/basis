import sys

from basis.lang.BasisLexer import BasisLexer
from basis.lang.BasisParser import BasisParser
from basis.lang.interpreter import Interpreter

from basis.eval.stdlib import STDOUT

from antlr4 import FileStream, CommonTokenStream

__all__ = ["interpret"]

def interpret(filepath):
    input_stream = FileStream(filepath)
    lexer = BasisLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BasisParser(stream)
    tree = parser.start()

    program = Interpreter().visit(tree)
    program.eval()

    return STDOUT.read()
