import sys

from basis.lang.BasisLexer import BasisLexer
from basis.lang.BasisParser import BasisParser
from basis.lang.interpreter import Interpreter

from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Trees import Trees

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

    program = Interpreter().visit(tree)
    program.eval()

if __name__ == "__main__":
    main()
