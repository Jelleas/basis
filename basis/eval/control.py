from . import Evaluable
from basis.data import *
import basis.logger as logger

__all__ = ["IfStatement", "IfElseStatement", "WhileLoop", "DoWhileLoop", "ForLoop"]


class IfStatement(Evaluable):
    def __init__(self, condition, code):
        self.condition = condition
        self.code = code

    def eval(self):
        with logger.context("IF-STMT") as log:
            log(f"if {self.condition}")

            if self.condition.eval().val:
                self.code.eval()


class IfElseStatement(Evaluable):
    def __init__(self, condition, if_code, else_code):
        self.condition = condition
        self.if_code = if_code
        self.else_code = else_code

    def eval(self):
        with logger.context("IF-STMT") as log:
            log(f"if {self.condition}")

            if self.condition.eval().val:
                self.if_code.eval()
                return

        with logger.context("ELSE-STMT") as log:
            log(f"else")
            self.else_code.eval()


class WhileLoop(Evaluable):
    def __init__(self, condition, code):
        self.condition = condition
        self.code = code

    def eval(self):
        with logger.context("WHILE-LOOP") as log:
            while True:
                log(f"while {logger.highlight(self.condition)}")
                if not self.condition.eval().val:
                    break

                self.code.eval()


class DoWhileLoop(Evaluable):
    def __init__(self, condition, code):
        self.code = code
        self.condition = condition

    def eval(self):
        with logger.context("DO-WHILE-LOOP") as log:
            while True:
                log("do")
                self.code.eval()

                log(f"while {logger.highlight(self.condition)}")
                if not self.condition.eval().val:
                    break


class ForLoop(Evaluable):
    def __init__(self, initialize, condition, update, code):
        self.initialize = initialize
        self.condition = condition
        self.update = update
        self.code = code

    def eval(self):
        with logger.context("FOR-LOOP") as log:
            log(f"for ({logger.highlight(self.initialize)}; {self.condition}; {self.update})")
            self.initialize.eval()

            while True:
                log(f"for ({self.initialize}; {logger.highlight(self.condition)}; {self.update})")
                if not self.condition.eval().val:
                    break

                self.code.eval()

                log(f"for ({self.initialize}; {self.condition}; {logger.highlight(self.update)})")
                self.update.eval()
