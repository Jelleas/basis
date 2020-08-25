from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener


class SyntaxError(Exception):
    pass


class BasisErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"{msg} on line: {line}, col: {column}")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass


# Remove the default ConsoleErrorListener
# https://github.com/antlr/antlr4/blob/be881fa6b91d1980936f8dcab902a9dc26ecd310/runtime/Python3/src/antlr4/error/ErrorListener.py#L27
ConsoleErrorListener.INSTANCE = ErrorListener()
