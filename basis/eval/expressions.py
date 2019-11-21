from . import Evaluable
from basis.data import *
import basis.logger as logger
from basis.lang.BasisLexer import BasisLexer

class BinaryExpr(Evaluable):
    COMPUTATIONS = {
        BasisLexer.TIMES: lambda l, r: l.mul(r),
        BasisLexer.DIV: lambda l, r: l.div(r),
        BasisLexer.PLUS: lambda l, r: l.add(r),
        BasisLexer.MINUS: lambda l, r: l.sub(r),
        BasisLexer.DUBEQ: lambda l, r: l.eq(r)
    }

    def __init__(self, ops, vals):
        self.ops = ops
        self.vals = vals

        for op in self.ops:
            if op.getPayload().type not in self.COMPUTATIONS:
                raise Exception(f"unknown operator {op}")

    def eval(self):
        vals = self.vals[::-1]
        ops = self.ops[::-1]

        with logger.context("BIN EXP") as log:
            left = vals.pop()
            log(self._format(ops[::-1], [str(val) for val in [left] + vals[::-1]]))
            left = left.eval()

            while vals:
                right = vals.pop().eval()
                op = ops.pop()
                comp = self.COMPUTATIONS[op.getPayload().type]
                left = comp(left, right)

                log(self._format(ops[::-1], [logger.emphasize(left)] + [str(val) for val in vals[::-1]]))

        return left

    def __str__(self):
        return f"({self._format(self.ops, [str(val) for val in self.vals])})"

    def _format(self, ops, vals):
        items = []
        for i in range(len(ops)):
            items.append(vals[i])
            items.append(ops[i].getText())
        items.append(vals[-1])
        return " ".join(items)


class UnaryExpr(Evaluable):
    COMPUTATIONS = {
        BasisLexer.PLUS: lambda r: r,
        BasisLexer.MINUS: lambda r: r.negate()
    }

    def __init__(self, op, right):
        self.op = op
        self.right = right

        self.computation = self.COMPUTATIONS.get(self.op.getPayload().type)

        if not self.computation:
            raise Exception(f"unknown op {self.op}")

    def eval(self):
        return self.computation(self.right.eval())

    def __str__(self):
        return f"{self.op.getText()}{self.right}"
