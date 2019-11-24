from antlr4 import *

from basis.lang.BasisVisitor import BasisVisitor
from basis.lang.BasisParser import BasisParser
from basis.lang.BasisLexer import BasisLexer

from eval import *

class EvalVisitor(BasisVisitor):
    def visitStart(self, ctx:BasisParser.StartContext):
        statements = []
        for child in ctx.getChildren():
            result = self.visit(child)
            if result:
                statements.append(result)
        return Block(statements)

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
        return Block(statements)

    def visitIf_statement(self, ctx:BasisParser.If_statementContext):
        children = list(ctx.getChildren())

        if len(children) == 3:
            _, comparison, code = children

            condition = self.visitComparison(comparison)
            code = self.visitBlock(code)

            return IfStatement(condition, code)
        else:
            _, comparison, if_code, _, else_code = children

            condition = self.visit(comparison)
            if_code = self.visit(if_code)
            else_code = self.visit(else_code)

            return IfElseStatement(condition, if_code, else_code)

    def visitFor_statement(self, ctx:BasisParser.For_statementContext):
        children = [child for child in ctx.getChildren() if not hasattr(child, "symbol")]
        children = [self.visit(child) for child in children]
        # Block should surround the entire for-loop
        return Block([ForLoop(*children[:-1], *children[-1].statements)])

    def visitFor_expression(self, ctx:BasisParser.For_expressionContext):
        children = [child for child in ctx.getChildren() if not hasattr(child, "symbol")]
        return Sequence([self.visit(child) for child in children])

    def visitAssignment(self, ctx:BasisParser.AssignmentContext):
        variable, _, val = tuple(ctx.getChildren())
        variable = variable.getText()
        val = self.visitChildren(val)
        return Assignment(variable, val)

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
        if ctx.BOOL():
            return BoolLiteral(text)
        if "." in text:
            return FloatLiteral(text)
        return IntLiteral(text)

    def visitVariable(self, ctx:BasisParser.VariableContext):
        return Variable(ctx.getText())

    def visitRelop(self, ctx:BasisParser.RelopContext):
        return next(ctx.getChildren())
