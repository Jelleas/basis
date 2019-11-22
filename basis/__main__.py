import sys

from antlr4 import *

from basis.lang.BasisLexer import BasisLexer
from basis.lang.BasisParser import BasisParser

from antlr4.tree.Trees import Trees

from basis.evaluator import EvalVisitor


def main():
    input_stream = FileStream(sys.argv[1])
    lexer = BasisLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BasisParser(stream)
    tree = parser.start()

    with open(sys.argv[1]) as f:
        print(f.read())

    # stream.fill()
    # for token in stream.getTokens(0, 10000):
    #     print(token, token.type)

    # print(Trees.toStringTree(tree, None, parser))

    evaluator = EvalVisitor().visit(tree)
    evaluator.eval()

if __name__ == "__main__":
    main()
