# Generated from basis/lang/Basis.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasisParser import BasisParser
else:
    from BasisParser import BasisParser

# This class defines a complete generic visitor for a parse tree produced by BasisParser.

class BasisVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasisParser#start.
    def visitStart(self, ctx:BasisParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#sequence.
    def visitSequence(self, ctx:BasisParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#statement.
    def visitStatement(self, ctx:BasisParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#block.
    def visitBlock(self, ctx:BasisParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#if_statement.
    def visitIf_statement(self, ctx:BasisParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#assignment.
    def visitAssignment(self, ctx:BasisParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#comparison.
    def visitComparison(self, ctx:BasisParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#expression.
    def visitExpression(self, ctx:BasisParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#term.
    def visitTerm(self, ctx:BasisParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#factor.
    def visitFactor(self, ctx:BasisParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#signedAtom.
    def visitSignedAtom(self, ctx:BasisParser.SignedAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#atom.
    def visitAtom(self, ctx:BasisParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#literal.
    def visitLiteral(self, ctx:BasisParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#variable.
    def visitVariable(self, ctx:BasisParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#relop.
    def visitRelop(self, ctx:BasisParser.RelopContext):
        return self.visitChildren(ctx)



del BasisParser