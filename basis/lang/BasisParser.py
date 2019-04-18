# Generated from basis/lang/Basis.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("O\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\5\2")
        buf.write("\34\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4%\n\4\f\4\16\4")
        buf.write("(\13\4\3\5\3\5\3\5\7\5-\n\5\f\5\16\5\60\13\5\3\6\3\6\3")
        buf.write("\6\7\6\65\n\6\f\6\16\68\13\6\3\7\3\7\3\7\3\7\3\7\5\7?")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\bG\n\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\5\3\2")
        buf.write("\7\b\3\2\t\n\3\2\13\r\2O\2\33\3\2\2\2\4\35\3\2\2\2\6!")
        buf.write("\3\2\2\2\b)\3\2\2\2\n\61\3\2\2\2\f>\3\2\2\2\16F\3\2\2")
        buf.write("\2\20H\3\2\2\2\22J\3\2\2\2\24L\3\2\2\2\26\34\5\4\3\2\27")
        buf.write("\34\5\6\4\2\30\34\5\b\5\2\31\34\5\n\6\2\32\34\5\f\7\2")
        buf.write("\33\26\3\2\2\2\33\27\3\2\2\2\33\30\3\2\2\2\33\31\3\2\2")
        buf.write("\2\33\32\3\2\2\2\34\3\3\2\2\2\35\36\5\6\4\2\36\37\5\24")
        buf.write("\13\2\37 \5\6\4\2 \5\3\2\2\2!&\5\b\5\2\"#\t\2\2\2#%\5")
        buf.write("\b\5\2$\"\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\7\3")
        buf.write("\2\2\2(&\3\2\2\2).\5\n\6\2*+\t\3\2\2+-\5\n\6\2,*\3\2\2")
        buf.write("\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\t\3\2\2\2\60.\3\2")
        buf.write("\2\2\61\66\5\f\7\2\62\63\7\17\2\2\63\65\5\f\7\2\64\62")
        buf.write("\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\13")
        buf.write("\3\2\2\28\66\3\2\2\29:\7\7\2\2:?\5\f\7\2;<\7\b\2\2<?\5")
        buf.write("\f\7\2=?\5\16\b\2>9\3\2\2\2>;\3\2\2\2>=\3\2\2\2?\r\3\2")
        buf.write("\2\2@G\5\20\t\2AG\5\22\n\2BC\7\5\2\2CD\5\6\4\2DE\7\6\2")
        buf.write("\2EG\3\2\2\2F@\3\2\2\2FA\3\2\2\2FB\3\2\2\2G\17\3\2\2\2")
        buf.write("HI\7\4\2\2I\21\3\2\2\2JK\7\3\2\2K\23\3\2\2\2LM\t\4\2\2")
        buf.write("M\25\3\2\2\2\b\33&.\66>F")
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
                      "POINT", "POW", "WS" ]

    RULE_start = 0
    RULE_equation = 1
    RULE_expression = 2
    RULE_term = 3
    RULE_factor = 4
    RULE_signedAtom = 5
    RULE_atom = 6
    RULE_literal = 7
    RULE_variable = 8
    RULE_relop = 9

    ruleNames =  [ "start", "equation", "expression", "term", "factor", 
                   "signedAtom", "atom", "literal", "variable", "relop" ]

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
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equation(self):
            return self.getTypedRuleContext(BasisParser.EquationContext,0)


        def expression(self):
            return self.getTypedRuleContext(BasisParser.ExpressionContext,0)


        def term(self):
            return self.getTypedRuleContext(BasisParser.TermContext,0)


        def factor(self):
            return self.getTypedRuleContext(BasisParser.FactorContext,0)


        def signedAtom(self):
            return self.getTypedRuleContext(BasisParser.SignedAtomContext,0)


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
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.term()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.factor()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 24
                self.signedAtom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EquationContext(ParserRuleContext):

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
            return BasisParser.RULE_equation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquation" ):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)




    def equation(self):

        localctx = BasisParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.expression()
            self.state = 28
            self.relop()
            self.state = 29
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

        def getRuleIndex(self):
            return BasisParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BasisParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.term()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasisParser.PLUS or _la==BasisParser.MINUS:
                self.state = 32
                _la = self._input.LA(1)
                if not(_la==BasisParser.PLUS or _la==BasisParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.term()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 6, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.factor()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasisParser.TIMES or _la==BasisParser.DIV:
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==BasisParser.TIMES or _la==BasisParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.factor()
                self.state = 46
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
        self.enterRule(localctx, 8, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.signedAtom()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasisParser.POW:
                self.state = 48
                self.match(BasisParser.POW)
                self.state = 49
                self.signedAtom()
                self.state = 54
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
        self.enterRule(localctx, 10, self.RULE_signedAtom)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.PLUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(BasisParser.PLUS)
                self.state = 56
                self.signedAtom()
                pass
            elif token in [BasisParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(BasisParser.MINUS)
                self.state = 58
                self.signedAtom()
                pass
            elif token in [BasisParser.VARIABLE, BasisParser.LITERAL, BasisParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
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
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.literal()
                pass
            elif token in [BasisParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.variable()
                pass
            elif token in [BasisParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(BasisParser.LPAREN)
                self.state = 65
                self.expression()
                self.state = 66
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
        self.enterRule(localctx, 14, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
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
        self.enterRule(localctx, 16, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
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

        def EQ(self):
            return self.getToken(BasisParser.EQ, 0)

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
        self.enterRule(localctx, 18, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasisParser.GT) | (1 << BasisParser.LT) | (1 << BasisParser.EQ))) != 0)):
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





