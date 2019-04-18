import sys
from antlr4 import *
from lang.BasisLexer import BasisLexer
from lang.BasisParser import BasisParser

from evaluator import EvalVisitor

input_stream = FileStream(sys.argv[1])
lexer = BasisLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = BasisParser(stream)
tree = parser.start()

runnable = EvalVisitor().visit(tree)
print(runnable.pretty_print())
print(runnable.eval().val)
