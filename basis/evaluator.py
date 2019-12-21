from antlr4 import *

from basis.lang.BasisVisitor import BasisVisitor
from basis.lang.BasisParser import BasisParser
from basis.lang.BasisLexer import BasisLexer

from eval import *

def _is_symbol(ctx):
    return hasattr(ctx, "symbol")

class EvalVisitor(BasisVisitor):
    def _visit_non_symbols(self, ctx):
        return [self.visit(child) for child in ctx.getChildren() if not _is_symbol(child)]

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

    def visitAnd_comparison(self, ctx:BasisParser.And_comparisonContext):
        return self.visitBinaryExpr(ctx)

    def visitEq_comparison(self, ctx:BasisParser.Eq_comparisonContext):
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
        children = self._visit_non_symbols(ctx)
        try:
            func_name, var_list, block = children
        except ValueError:
            func_name, block = children
            var_list = []
        return Function(func_name, var_list, block)

    def visitParameter_list(self, ctx:BasisParser.Parameter_listContext):
        vars = self._visit_non_symbols(ctx)

        if len(vars) == 1:
            return vars

        var_list, var = vars
        var_list.append(var)
        return var_list

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
        children = [child for child in ctx.getChildren() if not _is_symbol(child)]
        return Sequence([self.visit(child) for child in children])

    def visitAssignment(self, ctx:BasisParser.AssignmentContext):
        children = tuple(ctx.getChildren())
        if len(children) == 1:
            return self.visit(children[0])

        assignable, val = self._visit_non_symbols(ctx)
        return Assignment(assignable, val)

    def visitInline_assignment(self, ctx:BasisParser.Inline_assignmentContext):
        assignable, op, val = tuple(ctx.getChildren())
        assignable = self.visit(assignable)
        op = op.getPayload().type
        val = self.visit(val)
        return Assignment(assignable, BinaryExpr([op], [assignable, val]))

    def visitL_value(self, ctx:BasisParser.L_valueContext):
        return self.visitAtom_expression(ctx)

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

        assignable = self.visit(ctx.getChild(0))

        if ctx.getChild(1).getPayload().type == BasisLexer.INCREMENT:
            return PostIncrementAssignment(assignable)

        return PostDecrementAssignment(assignable)

    def visitPrecrement_expression(self, ctx:BasisParser.Precrement_expressionContext):
        if len(list(ctx.getChildren())) == 1:
            return self.visitChildren(ctx)

        assignable = self.visit(ctx.getChild(1))

        if ctx.getChild(0).getPayload().type == BasisLexer.INCREMENT:
            return PreIncrementAssignment(assignable)

        return PreDecrementAssignment(assignable)

    def visitAtom_expression(self, ctx:BasisParser.Atom_expressionContext):
        children = self._visit_non_symbols(ctx)
        atom = children[0]
        for child in children[1:]:
            # case of a function call
            if isinstance(child, list):
                atom = FunctionCall(atom, child)
            # case of an index expression
            else:
                atom = Index(atom, child)

        return atom

    def visitTrailer(self, ctx:BasisParser.TrailerContext):
        try:
            return self._visit_non_symbols(ctx)[0]
        except IndexError:
            return []

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
        if not _is_symbol(ctx.getChild(0)):
            return self.visit(ctx.getChild(0))
        if ctx.NULL():
            return NullLiteral()
        text = ctx.getText()
        if ctx.BOOL():
            return BoolLiteral(text)
        if ctx.STRING():
            return StringLiteral(text[1:-1])
        if "." in text:
            return FloatLiteral(text)
        return IntLiteral(text)

    def visitArray_literal(self, ctx:BasisParser.Array_literalContext):
        items = self._visit_non_symbols(ctx)
        return ArrayLiteral(items)

    def visitVariable(self, ctx:BasisParser.VariableContext):
        return Variable(ctx.getText())
