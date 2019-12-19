from . import Evaluable
from basis.data import *
import basis.logger as logger
from basis.lang.BasisLexer import BasisLexer

__all__ = ["BinaryExpr", "UnaryExpr"]


class BinaryExpr(Evaluable):
    COMPUTATIONS = {
        BasisLexer.MUL: lambda l, r: l.mul(r),
        BasisLexer.DIV: lambda l, r: l.div(r),
        BasisLexer.MOD: lambda l, r: l.mod(r),
        BasisLexer.ADD: lambda l, r: l.add(r),
        BasisLexer.SUB: lambda l, r: l.sub(r),
        BasisLexer.IADD: lambda l, r: l.add(r),
        BasisLexer.ISUB: lambda l, r: l.sub(r),
        BasisLexer.IMUL: lambda l, r: l.mul(r),
        BasisLexer.IDIV: lambda l, r: l.div(r),
        BasisLexer.IMOD: lambda l, r: l.mod(r),
        BasisLexer.DUBEQ: lambda l, r: l.eq(r),
        BasisLexer.NEQ: lambda l, r: l.neq(r),
        BasisLexer.GT: lambda l, r: l.gt(r),
        BasisLexer.LT: lambda l, r: l.lt(r),
        BasisLexer.GET: lambda l, r: l.get(r),
        BasisLexer.LET: lambda l, r: l.let(r),
        BasisLexer.AND: lambda l, r: l.and_(r),
        BasisLexer.OR: lambda l, r: l.or_(r)
    }

    REPRS = {
        BasisLexer.MUL: "*",
        BasisLexer.DIV: "/",
        BasisLexer.MOD: "%",
        BasisLexer.ADD: "+",
        BasisLexer.SUB: "-",
        BasisLexer.IADD: "+",
        BasisLexer.ISUB: "-",
        BasisLexer.IMUL: "*",
        BasisLexer.IDIV: "/",
        BasisLexer.IMOD: "%",
        BasisLexer.DUBEQ: "==",
        BasisLexer.NEQ: "!=",
        BasisLexer.GT: ">",
        BasisLexer.LT: "<",
        BasisLexer.GET: ">=",
        BasisLexer.LET: "<=",
        BasisLexer.AND: "&&",
        BasisLexer.OR: "||"
    }

    SHORT_CIRCUITS = {
        BasisLexer.AND: lambda val: not val.val,
        BasisLexer.OR: lambda val: val.val
    }

    def __init__(self, ops, vals):
        self.ops = ops
        self.vals = vals

        for op in self.ops:
            if op not in self.COMPUTATIONS:
                raise Exception(f"unknown operator {op}")

    def eval(self):
        vals = self.vals[::-1]
        ops = self.ops[::-1]

        with logger.context("BIN EXP") as log:
            log(self._format(ops[::-1], [str(val) for val in vals[::-1]]))
            left = vals.pop().eval()

            while vals:
                op = ops.pop()

                if op in self.SHORT_CIRCUITS and self.SHORT_CIRCUITS[op](left):
                    return left

                right = vals.pop().eval()
                comp = self.COMPUTATIONS[op]
                left = comp(left, right)

                log(self._format(ops[::-1], [logger.emphasize(left)] + [str(val) for val in vals[::-1]]))

        return left

    def __str__(self):
        return f"({self._format(self.ops, [str(val) for val in self.vals])})"

    def _format(self, ops, vals):
        items = []
        for i in range(len(ops)):
            items.append(vals[i])
            items.append(self.REPRS[ops[i]])
        items.append(vals[-1])
        return " ".join(items)


class UnaryExpr(Evaluable):
    COMPUTATIONS = {
        BasisLexer.ADD: lambda r: r,
        BasisLexer.SUB: lambda r: r.negate(),
        BasisLexer.NOT: lambda r: r.not_()
    }

    REPRS = {
        BasisLexer.ADD: "+",
        BasisLexer.SUB: "-",
        BasisLexer.NOT: "!"
    }

    def __init__(self, op, right):
        self.op = op
        self.right = right

        self.computation = self.COMPUTATIONS.get(self.op)

        if not self.computation:
            raise Exception(f"unknown op {self.op}")

    def eval(self):
        return self.computation(self.right.eval())

    def __str__(self):
        return f"{self.REPRS[self.op]}{self.right}"
