from antlr4 import *

from basis.lang.BasisVisitor import BasisVisitor
from basis.lang.BasisParser import BasisParser
from basis.lang.BasisLexer import BasisLexer

from eval import *

class EvalVisitor(BasisVisitor):
    def _visit_non_symbols(self, ctx):
        return [self.visit(child) for child in ctx.getChildren() if not hasattr(child, "symbol")]

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
        return self.visitBinaryExpr(ctx)

    def visitThen_comparison(self, ctx:BasisParser.Then_comparisonContext):
        return self.visitBinaryExpr(ctx)

    def visitNot_comparison(self, ctx:BasisParser.Not_comparisonContext):
        expr = self.visitChildren(ctx)
        if len(list(ctx.getChildren())) == 2:
            return UnaryExpr(ctx.getChild(0), expr)
        return expr

    def visitBlock(self, ctx:BasisParser.BlockContext):
        return Block(self._visit_non_symbols(ctx))

    def visitFunction_definition(self, ctx:BasisParser.Function_definitionContext):
        func_name, var_list, block = self._visit_non_symbols(ctx)
        return Function(func_name, var_list, block)

    def visitParameter_list(self, ctx:BasisParser.Parameter_listContext):
        vars = self._visit_non_symbols(ctx)

        if len(vars) == 1:
            return vars

        var_list, var = vars
        var_list.append(var)
        return var_list

    def visitFunction_call(self, ctx:BasisParser.Function_callContext):
        func_name, arg_list = self._visit_non_symbols(ctx)
        return FunctionCall(func_name, arg_list)

    def visitArgument_list(self, ctx:BasisParser.Argument_listContext):
        args = self._visit_non_symbols(ctx)

        if len(args) == 1:
            return args

        arg_list, arg = args
        arg_list.append(arg)
        return arg_list

    def visitIf_statement(self, ctx:BasisParser.If_statementContext):
        children = list(ctx.getChildren())

        if len(children) == 3:
            _, comparison, code = children

            condition = self.visit(comparison)
            code = self.visit(code)

            return Block([IfStatement(condition, code)])
        else:
            _, comparison, if_code, _, else_code = children

            condition = self.visit(comparison)
            if_code = self.visit(if_code)
            else_code = self.visit(else_code)

            return Block([IfElseStatement(condition, if_code, else_code)])

    def visitWhile_statement(self, ctx:BasisParser.While_statementContext):
        condition, block = self._visit_non_symbols(ctx)
        return Block([WhileLoop(condition, block)])

    def visitDo_while_statement(self, ctx:BasisParser.Do_while_statementContext):
        block, condition = self._visit_non_symbols(ctx)
        return Block([DoWhileLoop(block, condition)])

    def visitFor_statement(self, ctx:BasisParser.For_statementContext):
        initialize, condition, update, block = self._visit_non_symbols(ctx)
        return Block([ForLoop(initialize, condition, update, block)])

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
