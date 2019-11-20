from antlr4 import *

from basis.lang.BasisVisitor import BasisVisitor
from basis.lang.BasisParser import BasisParser
from basis.lang.BasisLexer import BasisLexer

from basis.data import *
from basis.stack import *

import basis.logger as logger


class Runnable:
    def eval(self):
        raise NotImplementedError()

    def pretty_print(self):
        raise NotImplementedError()


class BinaryExpr(Runnable):
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

    def pretty_print(self):
        return f"({self._format(self.ops, [val.pretty_print() for val in self.vals])})"

    def __str__(self):
        return f"({self._format(self.ops, [str(val) for val in self.vals])})"

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


class VariableExpr(Runnable):
    def __init__(self, variable, stack):
        self.variable = variable
        self.stack = stack

    def eval(self):
        with logger.context("Var Exp") as log:
            log(str(self.variable))
            result = self.stack[str(self.variable)]
            log(logger.emphasize(str(result)))
            return result

    def pretty_print(self):
        return str(self.variable)


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


class BoolLiteral(Runnable):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return Bool(self.val)

    def pretty_print(self):
        return str(self.val)

    def __str__(self):
        return f"B{self.val}"


class Assignment(Runnable):
    def __init__(self, variable, val, stack):
        self.variable = variable
        self.val = val
        self.stack = stack

    def eval(self):
        with logger.context("ASSIGNMENT") as log:
            log(f"{self.variable} = {self.val}")
            result = self.val.eval()
            self.stack.frames[-1][str(self.variable)] = result
            log(logger.emphasize(f"{self.variable} = {result}"))

    def pretty_print(self):
        return f"{self.variable} = {self.val.pretty_print()}"


class Block(Runnable):
    def __init__(self, statements, stack):
        self.statements = statements
        self.stack = stack

    def eval(self):
        self.stack.push(Frame())
        for statement in self.statements:
            statement.eval()
        self.stack.pop()

    def pretty_print(self):
        return "\n".join(s.pretty_print() for s in self.statements)


class IfStatement(Runnable):
    def __init__(self, condition, code):
        self.condition = condition
        self.code = code

    def eval(self):
        with logger.context("IF-STMT") as log:
            log(f"if {self.condition}")

            if self.condition.eval().val:
                self.code.eval()

    def pretty_print(self):
        # TODO
        return ""
        return f"if {self.condition.pretty_print()}\n    {self.code.pretty_print()}"


class EvalVisitor(BasisVisitor):
    def visitStart(self, ctx:BasisParser.StartContext):
        self.stack = Stack()
        return self.visitChildren(ctx)

    def visitSequence(self, ctx:BasisParser.SequenceContext):
        statements = []
        for child in ctx.getChildren():
            result = self.visitChildren(child)
            if result:
                statements.append(result)
        return Block(statements, self.stack)

    def visitStatement(self, ctx:BasisParser.StatementContext):
        return self.visitChildren(ctx)

    def visitComparison(self, ctx:BasisParser.ComparisonContext):
        children = list(ctx.getChildren())

        if len(children) == 1:
            return self.visit(children[0])

        ops = [self.visit(children[i + 1]) for i in range(0, len(children) - 1, 2)]
        vals = [self.visit(children[i]) for i in range(0, len(children), 2)]
        return BinaryExpr(ops, vals)

    def visitBlock(self, ctx:BasisParser.BlockContext):
        statements = []
        for child in ctx.getChildren():
            result = self.visitChildren(child)
            if result:
                statements.append(result)
        return Block(statements, self.stack)

    def visitIf_statement(self, ctx:BasisParser.If_statementContext):
        _, comparison, block = ctx.getChildren()

        condition = self.visitComparison(comparison)
        code = self.visitBlock(block)

        return IfStatement(condition, code)

    def visitAssignment(self, ctx:BasisParser.AssignmentContext):
        variable, _, val = tuple(ctx.getChildren())
        variable = variable.getText()
        val = self.visitChildren(val)
        return Assignment(variable, val, self.stack)

    def visitExpression(self, ctx:BasisParser.ExpressionContext):
        return self.visitBinaryExpr(ctx)

    def visitTerm(self, ctx:BasisParser.TermContext):
        return self.visitBinaryExpr(ctx)

    def visitBinaryExpr(self, ctx:BasisParser.FactorContext):
        children = list(ctx.getChildren())

        if len(children) == 1:
            return self.visit(children[0])

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
        children = list(ctx.getChildren())

        if len(children) == 1:
            return self.visit(children[0])

        return self.visit(children[1])

    def visitLiteral(self, ctx:BasisParser.LiteralContext):
        text = ctx.getText()
        if "." in text:
            return FloatLiteral(text)
        if ctx.BOOL():
            return BoolLiteral(text)
        return IntLiteral(text)

    def visitVariable(self, ctx:BasisParser.VariableContext):
        return VariableExpr(ctx.getText(), self.stack)

    def visitRelop(self, ctx:BasisParser.RelopContext):
        return next(ctx.getChildren())
