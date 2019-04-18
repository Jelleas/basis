from antlr4 import *

from lang.BasisVisitor import BasisVisitor
from lang.BasisParser import BasisParser
from lang.BasisLexer import BasisLexer

from data import *

class Runnable:
    def eval(self):
        raise NotImplementedError()

    def pretty_print(self):
        raise NotImplementedError()

    # def __str__(self):
    #     return str(self.pretty_print())


class BinaryExpr(Runnable):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

        if self.op.getPayload().type == BasisLexer.TIMES:
            self._compute = lambda l, r: l.mul(r)
        elif self.op.getPayload().type == BasisLexer.DIV:
            self._compute = lambda l, r: l.div(r)
        else:
            raise Exception(f"unknown op {self.op}")

    def eval(self):
        return self._compute(self.left.eval(), self.right.eval())

    def pretty_print(self):
        return f"({self.left.pretty_print()} {self.op.getText()} {self.right.pretty_print()})"


class UnaryExpr(Runnable):
    def __init__(self, op, right):
        self.op = op
        self.right = right

        if self.op.getPayload().type == BasisLexer.MINUS:
            self._compute = lambda r: r.negate()
        elif self.op.getPayload().type == BasisLexer.PLUS:
            self._compute = lambda r: r
        else:
            raise Exception(f"unknown op {self.op}")

    def eval(self):
        return self._compute(self.right.eval())

    def pretty_print(self):
        return f"({self.op.getText()}{self.right.pretty_print()})"


class IntLiteral(Runnable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Int(self.val)

    def pretty_print(self):
        return str(self.val)


class FloatLiteral(Runnable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Float(self.val)

    def pretty_print(self):
        return str(self.val)


class EvalVisitor(BasisVisitor):
    def visitStart(self, ctx:BasisParser.StartContext):
        return self.visitChildren(ctx)

    def visitEquation(self, ctx:BasisParser.EquationContext):
        return self.visitChildren(ctx)

    def visitExpression(self, ctx:BasisParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitTerm(self, ctx:BasisParser.TermContext):
        children = list(ctx.getChildren())

        expr = self.visit(children[0])

        for i in range(1, len(children), 2):
            op = children[i]
            right = self.visit(children[i + 1])
            expr = BinaryExpr(expr, op, right)

        return expr

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

    def visitNumber(self, ctx):
        print("foo")
        return 3
