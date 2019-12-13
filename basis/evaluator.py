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
        children = ctx.getChildren()

        # skip if symbol
        next(children)

        condition = self.visit(next(children))

        try:
            code = self.visit(next(children))
        except StopIteration:
            # Case: if condition
            return Block([IfStatement(condition, NoOp())])

        # if code was just the NEWLINE symbol
        if code == None:
            code = NoOp()

        try:
            # visit else_statement
            else_code = self.visit(next(children))
        except StopIteration:
            # Case: if condition block
            return Block([IfStatement(condition, code)])

        # if else_statement was just the else symbol
        if else_code == None:
            else_code = NoOp()

        # Case: if condition (NewLine|block?) else_statement
        return Block([IfElseStatement(condition, code, else_code)])

    def visitElse_statement(self, ctx:BasisParser.Else_statementContext):
        return self.visitChildren(ctx)

    def visitWhile_statement(self, ctx:BasisParser.While_statementContext):
        evals = self._visit_non_symbols(ctx)
        try:
            condition, block = evals
        except ValueError:
            condition, block = evals[0], NoOp()
        return Block([WhileLoop(condition, block)])

    def visitDo_while_statement(self, ctx:BasisParser.Do_while_statementContext):
        evals = self._visit_non_symbols(ctx)
        try:
            block, condition = evals
        except ValueError:
            block, condition = NoOp(), evals[0]
        return Block([DoWhileLoop(block, condition)])

    def visitFor_statement(self, ctx:BasisParser.For_statementContext):
        children = ctx.getChildren()

        # skip for symbol
        next(children)
        # skip LPAREN symbol
        next(children)

        initialize = self.visit(next(children))

        if initialize == None:
            initialize = NoOp()
        else:
            # skip ; symbol
            next(children)

        condition = self.visit(next(children))

        # skip ; symbol
        next(children)

        update = self.visit(next(children))

        if update == None:
            update = NoOp()
        else:
            # skip RPAREN symbol
            next(children)

        try:
            block = self.visit(next(children))
        except StopIteration:
            block = NoOp()

        return Block([ForLoop(initialize, condition, update, block)])

    def visitFor_expression(self, ctx:BasisParser.For_expressionContext):
        children = [child for child in ctx.getChildren() if not hasattr(child, "symbol")]
        return Sequence([self.visit(child) for child in children])

    def visitAssignment(self, ctx:BasisParser.AssignmentContext):
        children = tuple(ctx.getChildren())
        if len(children) == 1:
            return self.visit(children[0])

        variable, _, val = tuple(ctx.getChildren())
        variable = variable.getText()
        val = self.visitChildren(val)
        return Assignment(variable, val)

    def visitI_assignment(self, ctx:BasisParser.I_assignmentContext):
        variable, op, val = tuple(ctx.getChildren())
        variable = variable.getText()
        op = op.getPayload().type
        val = self.visitChildren(val)
        return Assignment(variable, BinaryExpr([op], [Variable(variable), val]))

    def visitExpression(self, ctx:BasisParser.ExpressionContext):
        return self.visitBinaryExpr(ctx)

    def visitTerm(self, ctx:BasisParser.TermContext):
        return self.visitBinaryExpr(ctx)

    def visitBinaryExpr(self, ctx:BasisParser.TermContext):
        children = list(ctx.getChildren())

        if len(children) == 1:
            return self.visit(children[0])

        ops = [children[i + 1].getPayload().type for i in range(0, len(children) - 1, 2)]
        vals = [self.visit(children[i]) for i in range(0, len(children), 2)]
        return BinaryExpr(ops, vals)

    def visitSignedAtom(self, ctx:BasisParser.SignedAtomContext):
        expr = self.visitChildren(ctx)
        if len(list(ctx.getChildren())) == 2:
            return UnaryExpr(ctx.getChild(0).getPayload().type, expr)
        return expr

    def visitPostcrement_expression(self, ctx:BasisParser.Postcrement_expressionContext):
        if len(list(ctx.getChildren())) == 1:
            return self.visitChildren(ctx)

        variable = self.visit(ctx.getChild(0))

        if ctx.getChild(1).getPayload().type == BasisLexer.INCREMENT:
            return PostIncrementAssignment(variable)

        return PostDecrementAssignment(variable)

    def visitPrecrement_expression(self, ctx:BasisParser.Precrement_expressionContext):
        if len(list(ctx.getChildren())) == 1:
            return self.visitChildren(ctx)

        variable = self.visit(ctx.getChild(1))

        if ctx.getChild(0).getPayload().type == BasisLexer.INCREMENT:
            return PreIncrementAssignment(variable)

        return PreDecrementAssignment(variable)

    def visitAtom(self, ctx:BasisParser.AtomContext):
        children = list(ctx.getChildren())

        if len(children) == 1:
            return self.visit(children[0])
        return self.visit(children[1])

    def visitBreak_(self, ctx:BasisParser.Break_Context):
        return Break()

    def visitContinue_(self, ctx:BasisParser.Continue_Context):
        return Continue()

    def visitReturn_(self, ctx:BasisParser.Return_Context):
        children = list(ctx.getChildren())
        if len(children) == 1:
            print(children)
            return Return(NoOp())
        return Return(self.visit(children[1]))

    def visitLiteral(self, ctx:BasisParser.LiteralContext):
        text = ctx.getText()
        if ctx.NULL():
            return NullLiteral()
        if ctx.BOOL():
            return BoolLiteral(text)
        if ctx.STRING():
            return StringLiteral(text)
        if "." in text:
            return FloatLiteral(text)
        return IntLiteral(text)

    def visitVariable(self, ctx:BasisParser.VariableContext):
        return Variable(ctx.getText())
