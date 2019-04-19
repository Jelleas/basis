from antlr4 import *

from lang.BasisVisitor import BasisVisitor
from lang.BasisParser import BasisParser
from lang.BasisLexer import BasisLexer

from data import *

import logger


class Runnable:
    def eval(self):
        raise NotImplementedError()

    def pretty_print(self):
        raise NotImplementedError()

    # def __str__(self):
    #     return str(self.pretty_print())


class BinaryExpr(Runnable):
    COMPUTATIONS = {
        BasisLexer.TIMES: lambda l, r: l.mul(r),
        BasisLexer.DIV: lambda l, r: l.div(r),
        BasisLexer.PLUS: lambda l, r: l.add(r),
        BasisLexer.MINUS: lambda l, r: l.sub(r),
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

    def pretty_print(self):
        return f"({self._format(self.ops, [val.pretty_print() for val in self.vals])})"

    def __str__(self):
        return self._format(self.ops, [str(val) for val in self.vals])

    def _format(self, ops, vals):
        items = []
        for i in range(len(ops)):
            items.append(vals[i])
            items.append(ops[i].getText())
        items.append(vals[-1])
        return " ".join(items)


class UnaryExpr(Runnable):
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

    def pretty_print(self):
        return f"({self.op.getText()}{self.right.pretty_print()})"

    def __str__(self):
        return f"{self.op.getText()}{self.right}"


class IntLiteral(Runnable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Int(self.val)

    def pretty_print(self):
        return str(self.val)

    def __str__(self):
        return f"I{self.val}"


class FloatLiteral(Runnable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Float(self.val)

    def pretty_print(self):
        return str(self.val)

    def __str__(self):
        return f"F{self.val}"


class EvalVisitor(BasisVisitor):
    def visitStart(self, ctx:BasisParser.StartContext):
        return self.visitChildren(ctx)

    def visitEquation(self, ctx:BasisParser.EquationContext):
        return self.visitChildren(ctx)

    def visitExpression(self, ctx:BasisParser.ExpressionContext):
        return self.visitBinaryExpr(ctx)

    def visitTerm(self, ctx:BasisParser.TermContext):
        return self.visitBinaryExpr(ctx)

    def visitBinaryExpr(self, ctx:BasisParser.FactorContext):
        children = list(ctx.getChildren())

        if len(children) == 1:
            return self.visitChildren(ctx)

        ops = [children[i + 1] for i in range(0, len(children) - 1, 2)]
        vals = [self.visit(children[i]) for i in range(0, len(children), 2)]
        return BinaryExpr(ops, vals)

    def visitFactor(self, ctx:BasisParser.FactorContext):
        return self.visitChildren(ctx)

    def visitSignedAtom(self, ctx:BasisParser.SignedAtomContext):
        expr = self.visitChildren(ctx)
        if len(list(ctx.getChildren())) == 2:
            return UnaryExpr(ctx.getChild(0), expr)
        return expr

    def visitAtom(self, ctx:BasisParser.AtomContext):
        return self.visitChildren(ctx)

    def visitLiteral(self, ctx:BasisParser.LiteralContext):
        text = ctx.getText()
        if "." in text:
            return FloatLiteral(text)
        return IntLiteral(text)

    def visitVariable(self, ctx:BasisParser.VariableContext):
        return self.visitChildren(ctx)

    def visitRelop(self, ctx:BasisParser.RelopContext):
        return self.visitChildren(ctx)
