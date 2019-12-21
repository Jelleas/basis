import sys
import argparse
import basis.logger as logger

from basis.lang.BasisLexer import BasisLexer
from basis.lang.BasisParser import BasisParser
from basis.lang.interpreter import Interpreter

from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Trees import Trees

def main():
    parser = argparse.ArgumentParser(prog="basis")
    parser.add_argument("file",
                        help="file to execute")
    parser.add_argument("-v", "--verbose",
                        action="store_true",
                        help="print the code and the log")
    args = parser.parse_args()

    if args.verbose:
        with open(args.file) as f:
            print(f.read())
        logger.enable()

    input_stream = FileStream(args.file)
    lexer = BasisLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BasisParser(stream)
    tree = parser.start()

    # stream.fill()
    # for token in stream.getTokens(0, 10000):
    #     print(token, token.type)

    # print(Trees.toStringTree(tree, None, parser))

    program = Interpreter().visit(tree)
    program.eval()

if __name__ == "__main__":
    main()
