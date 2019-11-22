from . import Evaluable
from basis.data import *
import basis.logger as logger


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
