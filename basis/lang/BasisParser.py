# Generated from basis/lang/Basis.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("j\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\3\3\3\3\3\7\3\"\n\3\f\3\16\3%\13\3\3\4\3")
        buf.write("\4\3\4\5\4*\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\64")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7=\n\7\f\7\16\7@\13")
        buf.write("\7\3\7\5\7C\n\7\3\b\3\b\3\b\7\bH\n\b\f\b\16\bK\13\b\3")
        buf.write("\t\3\t\3\t\7\tP\n\t\f\t\16\tS\13\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\5\nZ\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13b\n\13\3\f")
        buf.write("\3\f\3\r\3\r\3\16\3\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\2\5\3\2\7\b\3\2\t\n\3\2\13\f\2h\2\34\3\2")
        buf.write("\2\2\4\36\3\2\2\2\6)\3\2\2\2\b\63\3\2\2\2\n\65\3\2\2\2")
        buf.write("\fB\3\2\2\2\16D\3\2\2\2\20L\3\2\2\2\22Y\3\2\2\2\24a\3")
        buf.write("\2\2\2\26c\3\2\2\2\30e\3\2\2\2\32g\3\2\2\2\34\35\5\4\3")
        buf.write("\2\35\3\3\2\2\2\36#\5\6\4\2\37 \7\20\2\2 \"\5\6\4\2!\37")
        buf.write("\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\5\3\2\2\2%#\3")
        buf.write("\2\2\2&*\5\f\7\2\'*\5\n\6\2(*\5\b\5\2)&\3\2\2\2)\'\3\2")
        buf.write("\2\2)(\3\2\2\2*\7\3\2\2\2+,\5\30\r\2,-\7\r\2\2-.\5\f\7")
        buf.write("\2.\64\3\2\2\2/\60\5\30\r\2\60\61\7\r\2\2\61\62\5\n\6")
        buf.write("\2\62\64\3\2\2\2\63+\3\2\2\2\63/\3\2\2\2\64\t\3\2\2\2")
        buf.write("\65\66\5\f\7\2\66\67\5\32\16\2\678\5\f\7\28\13\3\2\2\2")
        buf.write("9>\5\16\b\2:;\t\2\2\2;=\5\16\b\2<:\3\2\2\2=@\3\2\2\2>")
        buf.write("<\3\2\2\2>?\3\2\2\2?C\3\2\2\2@>\3\2\2\2AC\5\30\r\2B9\3")
        buf.write("\2\2\2BA\3\2\2\2C\r\3\2\2\2DI\5\20\t\2EF\t\3\2\2FH\5\20")
        buf.write("\t\2GE\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\17\3\2\2")
        buf.write("\2KI\3\2\2\2LQ\5\22\n\2MN\7\17\2\2NP\5\22\n\2OM\3\2\2")
        buf.write("\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\21\3\2\2\2SQ\3\2\2\2")
        buf.write("TU\7\7\2\2UZ\5\22\n\2VW\7\b\2\2WZ\5\22\n\2XZ\5\24\13\2")
        buf.write("YT\3\2\2\2YV\3\2\2\2YX\3\2\2\2Z\23\3\2\2\2[b\5\26\f\2")
        buf.write("\\b\5\30\r\2]^\7\5\2\2^_\5\f\7\2_`\7\6\2\2`b\3\2\2\2a")
        buf.write("[\3\2\2\2a\\\3\2\2\2a]\3\2\2\2b\25\3\2\2\2cd\7\4\2\2d")
        buf.write("\27\3\2\2\2ef\7\3\2\2f\31\3\2\2\2gh\t\4\2\2h\33\3\2\2")
        buf.write("\2\13#)\63>BIQYa")
        return buf.getvalue()


class BasisParser ( Parser ):

    grammarFileName = "Basis.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'='", "'.'", 
                     "'^'" ]

    symbolicNames = [ "<INVALID>", "VARIABLE", "LITERAL", "LPAREN", "RPAREN", 
                      "PLUS", "MINUS", "TIMES", "DIV", "GT", "LT", "EQ", 
                      "POINT", "POW", "NEWLINE", "WS" ]

    RULE_start = 0
    RULE_sequence = 1
    RULE_statement = 2
    RULE_assignment = 3
    RULE_comparison = 4
    RULE_expression = 5
    RULE_term = 6
    RULE_factor = 7
    RULE_signedAtom = 8
    RULE_atom = 9
    RULE_literal = 10
    RULE_variable = 11
    RULE_relop = 12

    ruleNames =  [ "start", "sequence", "statement", "assignment", "comparison", 
                   "expression", "term", "factor", "signedAtom", "atom", 
                   "literal", "variable", "relop" ]

    EOF = Token.EOF
    VARIABLE=1
    LITERAL=2
    LPAREN=3
    RPAREN=4
    PLUS=5
    MINUS=6
    TIMES=7
    DIV=8
    GT=9
    LT=10
    EQ=11
    POINT=12
    POW=13
    NEWLINE=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequence(self):
            return self.getTypedRuleContext(BasisParser.SequenceContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = BasisParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasisParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.NEWLINE)
            else:
                return self.getToken(BasisParser.NEWLINE, i)

        def getRuleIndex(self):
            return BasisParser.RULE_sequence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = BasisParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.statement()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasisParser.NEWLINE:
                self.state = 29
                self.match(BasisParser.NEWLINE)
                self.state = 30
                self.statement()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BasisParser.ExpressionContext,0)


        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def assignment(self):
            return self.getTypedRuleContext(BasisParser.AssignmentContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BasisParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.comparison()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BasisParser.VariableContext,0)


        def EQ(self):
            return self.getToken(BasisParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(BasisParser.ExpressionContext,0)


        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = BasisParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.variable()
                self.state = 42
                self.match(BasisParser.EQ)
                self.state = 43
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.variable()
                self.state = 46
                self.match(BasisParser.EQ)
                self.state = 47
                self.comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasisParser.ExpressionContext,i)


        def relop(self):
            return self.getTypedRuleContext(BasisParser.RelopContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = BasisParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.expression()
            self.state = 52
            self.relop()
            self.state = 53
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.TermContext)
            else:
                return self.getTypedRuleContext(BasisParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.PLUS)
            else:
                return self.getToken(BasisParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.MINUS)
            else:
                return self.getToken(BasisParser.MINUS, i)

        def variable(self):
            return self.getTypedRuleContext(BasisParser.VariableContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BasisParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.term()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BasisParser.PLUS or _la==BasisParser.MINUS:
                    self.state = 56
                    _la = self._input.LA(1)
                    if not(_la==BasisParser.PLUS or _la==BasisParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 57
                    self.term()
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.FactorContext)
            else:
                return self.getTypedRuleContext(BasisParser.FactorContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.TIMES)
            else:
                return self.getToken(BasisParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.DIV)
            else:
                return self.getToken(BasisParser.DIV, i)

        def getRuleIndex(self):
            return BasisParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = BasisParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.factor()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasisParser.TIMES or _la==BasisParser.DIV:
                self.state = 67
                _la = self._input.LA(1)
                if not(_la==BasisParser.TIMES or _la==BasisParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 68
                self.factor()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signedAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.SignedAtomContext)
            else:
                return self.getTypedRuleContext(BasisParser.SignedAtomContext,i)


        def POW(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.POW)
            else:
                return self.getToken(BasisParser.POW, i)

        def getRuleIndex(self):
            return BasisParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = BasisParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.signedAtom()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasisParser.POW:
                self.state = 75
                self.match(BasisParser.POW)
                self.state = 76
                self.signedAtom()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedAtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(BasisParser.PLUS, 0)

        def signedAtom(self):
            return self.getTypedRuleContext(BasisParser.SignedAtomContext,0)


        def MINUS(self):
            return self.getToken(BasisParser.MINUS, 0)

        def atom(self):
            return self.getTypedRuleContext(BasisParser.AtomContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_signedAtom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignedAtom" ):
                return visitor.visitSignedAtom(self)
            else:
                return visitor.visitChildren(self)




    def signedAtom(self):

        localctx = BasisParser.SignedAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_signedAtom)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.PLUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(BasisParser.PLUS)
                self.state = 83
                self.signedAtom()
                pass
            elif token in [BasisParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(BasisParser.MINUS)
                self.state = 85
                self.signedAtom()
                pass
            elif token in [BasisParser.VARIABLE, BasisParser.LITERAL, BasisParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BasisParser.LiteralContext,0)


        def variable(self):
            return self.getTypedRuleContext(BasisParser.VariableContext,0)


        def LPAREN(self):
            return self.getToken(BasisParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasisParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasisParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasisParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = BasisParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atom)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.literal()
                pass
            elif token in [BasisParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.variable()
                pass
            elif token in [BasisParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(BasisParser.LPAREN)
                self.state = 92
                self.expression()
                self.state = 93
                self.match(BasisParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self):
            return self.getToken(BasisParser.LITERAL, 0)

        def getRuleIndex(self):
            return BasisParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BasisParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(BasisParser.LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(BasisParser.VARIABLE, 0)

        def getRuleIndex(self):
            return BasisParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BasisParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(BasisParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(BasisParser.GT, 0)

        def LT(self):
            return self.getToken(BasisParser.LT, 0)

        def getRuleIndex(self):
            return BasisParser.RULE_relop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = BasisParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            _la = self._input.LA(1)
            if not(_la==BasisParser.GT or _la==BasisParser.LT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





