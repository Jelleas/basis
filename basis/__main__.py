import sys

from antlr4 import *

from basis.lang.BasisLexer import BasisLexer
from basis.lang.BasisParser import BasisParser

from basis.evaluator import EvalVisitor


def main():
    input_stream = FileStream(sys.argv[1])
    lexer = BasisLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BasisParser(stream)
    tree = parser.start()

    runnable = EvalVisitor().visit(tree)
    print(runnable.pretty_print())
    runnable.eval()

if __name__ == "__main__":
    main()
