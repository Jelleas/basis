# Generated from basis/lang/Basis.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("g\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\7\2,\n\2\f\2\16\2/\13\2\3\3\5\3\62")
        buf.write("\n\3\3\4\3\4\5\4\66\n\4\3\5\3\5\3\6\6\6;\n\6\r\6\16\6")
        buf.write("<\3\6\3\6\6\6A\n\6\r\6\16\6B\5\6E\n\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\6\24b\n\24\r\24\16\24c\3\24\3\24\2\2\25\3\3\5\2\7\2\t")
        buf.write("\4\13\2\r\2\17\2\21\5\23\6\25\7\27\b\31\t\33\n\35\13\37")
        buf.write("\f!\r#\16%\17\'\20\3\2\6\5\2C\\aac|\4\2GGgg\4\2--//\5")
        buf.write("\2\13\f\17\17\"\"\2g\2\3\3\2\2\2\2\t\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5\61\3\2\2")
        buf.write("\2\7\65\3\2\2\2\t\67\3\2\2\2\13:\3\2\2\2\rF\3\2\2\2\17")
        buf.write("H\3\2\2\2\21J\3\2\2\2\23L\3\2\2\2\25N\3\2\2\2\27P\3\2")
        buf.write("\2\2\31R\3\2\2\2\33T\3\2\2\2\35V\3\2\2\2\37X\3\2\2\2!")
        buf.write("Z\3\2\2\2#\\\3\2\2\2%^\3\2\2\2\'a\3\2\2\2)-\5\5\3\2*,")
        buf.write("\5\7\4\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\4\3")
        buf.write("\2\2\2/-\3\2\2\2\60\62\t\2\2\2\61\60\3\2\2\2\62\6\3\2")
        buf.write("\2\2\63\66\5\5\3\2\64\66\4\62;\2\65\63\3\2\2\2\65\64\3")
        buf.write("\2\2\2\66\b\3\2\2\2\678\5\13\6\28\n\3\2\2\29;\4\62;\2")
        buf.write(":9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=D\3\2\2\2>@\7")
        buf.write("\60\2\2?A\4\62;\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2")
        buf.write("\2\2CE\3\2\2\2D>\3\2\2\2DE\3\2\2\2E\f\3\2\2\2FG\t\3\2")
        buf.write("\2G\16\3\2\2\2HI\t\4\2\2I\20\3\2\2\2JK\7*\2\2K\22\3\2")
        buf.write("\2\2LM\7+\2\2M\24\3\2\2\2NO\7-\2\2O\26\3\2\2\2PQ\7/\2")
        buf.write("\2Q\30\3\2\2\2RS\7,\2\2S\32\3\2\2\2TU\7\61\2\2U\34\3\2")
        buf.write("\2\2VW\7@\2\2W\36\3\2\2\2XY\7>\2\2Y \3\2\2\2Z[\7?\2\2")
        buf.write("[\"\3\2\2\2\\]\7\60\2\2]$\3\2\2\2^_\7`\2\2_&\3\2\2\2`")
        buf.write("b\t\5\2\2a`\3\2\2\2bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2de\3")
        buf.write("\2\2\2ef\b\24\2\2f(\3\2\2\2\n\2-\61\65<BDc\3\b\2\2")
        return buf.getvalue()


class BasisLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VARIABLE = 1
    LITERAL = 2
    LPAREN = 3
    RPAREN = 4
    PLUS = 5
    MINUS = 6
    TIMES = 7
    DIV = 8
    GT = 9
    LT = 10
    EQ = 11
    POINT = 12
    POW = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'='", 
            "'.'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "VARIABLE", "LITERAL", "LPAREN", "RPAREN", "PLUS", "MINUS", 
            "TIMES", "DIV", "GT", "LT", "EQ", "POINT", "POW", "WS" ]

    ruleNames = [ "VARIABLE", "VALID_ID_START", "VALID_ID_CHAR", "LITERAL", 
                  "NUMBER", "E", "SIGN", "LPAREN", "RPAREN", "PLUS", "MINUS", 
                  "TIMES", "DIV", "GT", "LT", "EQ", "POINT", "POW", "WS" ]

    grammarFileName = "Basis.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


