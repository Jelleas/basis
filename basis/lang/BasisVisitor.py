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


    # Visit a parse tree produced by BasisParser#statement.
    def visitStatement(self, ctx:BasisParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#block.
    def visitBlock(self, ctx:BasisParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#function_definition.
    def visitFunction_definition(self, ctx:BasisParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#parameter_list.
    def visitParameter_list(self, ctx:BasisParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#function_call.
    def visitFunction_call(self, ctx:BasisParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#argument_list.
    def visitArgument_list(self, ctx:BasisParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#if_statement.
    def visitIf_statement(self, ctx:BasisParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#else_statement.
    def visitElse_statement(self, ctx:BasisParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#while_statement.
    def visitWhile_statement(self, ctx:BasisParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BasisParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#for_statement.
    def visitFor_statement(self, ctx:BasisParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#for_expression.
    def visitFor_expression(self, ctx:BasisParser.For_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#assignment.
    def visitAssignment(self, ctx:BasisParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#comparison.
    def visitComparison(self, ctx:BasisParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#then_comparison.
    def visitThen_comparison(self, ctx:BasisParser.Then_comparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#not_comparison.
    def visitNot_comparison(self, ctx:BasisParser.Not_comparisonContext):
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


    # Visit a parse tree produced by BasisParser#postcrement_expression.
    def visitPostcrement_expression(self, ctx:BasisParser.Postcrement_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#precrement_expression.
    def visitPrecrement_expression(self, ctx:BasisParser.Precrement_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#atom.
    def visitAtom(self, ctx:BasisParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#break_.
    def visitBreak_(self, ctx:BasisParser.Break_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#continue_.
    def visitContinue_(self, ctx:BasisParser.Continue_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#return_.
    def visitReturn_(self, ctx:BasisParser.Return_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#literal.
    def visitLiteral(self, ctx:BasisParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#variable.
    def visitVariable(self, ctx:BasisParser.VariableContext):
        return self.visitChildren(ctx)



del BasisParser