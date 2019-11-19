# Generated from basis/lang/Basis.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("n\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\7\2.\n\2\f\2\16\2\61\13\2")
        buf.write("\3\3\5\3\64\n\3\3\4\3\4\5\48\n\4\3\5\3\5\3\6\6\6=\n\6")
        buf.write("\r\6\16\6>\3\6\3\6\6\6C\n\6\r\6\16\6D\5\6G\n\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\24\5\24f\n\24\3\25\6\25i\n\25\r\25\16\25")
        buf.write("j\3\25\3\25\2\2\26\3\3\5\2\7\2\t\4\13\2\r\2\17\2\21\5")
        buf.write("\23\6\25\7\27\b\31\t\33\n\35\13\37\f!\r#\16%\17\'\20)")
        buf.write("\21\3\2\6\5\2C\\aac|\4\2GGgg\4\2--//\4\2\13\13\"\"\2o")
        buf.write("\2\3\3\2\2\2\2\t\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5\63\3\2\2\2\7\67\3\2")
        buf.write("\2\2\t9\3\2\2\2\13<\3\2\2\2\rH\3\2\2\2\17J\3\2\2\2\21")
        buf.write("L\3\2\2\2\23N\3\2\2\2\25P\3\2\2\2\27R\3\2\2\2\31T\3\2")
        buf.write("\2\2\33V\3\2\2\2\35X\3\2\2\2\37Z\3\2\2\2!\\\3\2\2\2#^")
        buf.write("\3\2\2\2%`\3\2\2\2\'e\3\2\2\2)h\3\2\2\2+/\5\5\3\2,.\5")
        buf.write("\7\4\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60")
        buf.write("\4\3\2\2\2\61/\3\2\2\2\62\64\t\2\2\2\63\62\3\2\2\2\64")
        buf.write("\6\3\2\2\2\658\5\5\3\2\668\4\62;\2\67\65\3\2\2\2\67\66")
        buf.write("\3\2\2\28\b\3\2\2\29:\5\13\6\2:\n\3\2\2\2;=\4\62;\2<;")
        buf.write("\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?F\3\2\2\2@B\7\60")
        buf.write("\2\2AC\4\62;\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2")
        buf.write("EG\3\2\2\2F@\3\2\2\2FG\3\2\2\2G\f\3\2\2\2HI\t\3\2\2I\16")
        buf.write("\3\2\2\2JK\t\4\2\2K\20\3\2\2\2LM\7*\2\2M\22\3\2\2\2NO")
        buf.write("\7+\2\2O\24\3\2\2\2PQ\7-\2\2Q\26\3\2\2\2RS\7/\2\2S\30")
        buf.write("\3\2\2\2TU\7,\2\2U\32\3\2\2\2VW\7\61\2\2W\34\3\2\2\2X")
        buf.write("Y\7@\2\2Y\36\3\2\2\2Z[\7>\2\2[ \3\2\2\2\\]\7?\2\2]\"\3")
        buf.write("\2\2\2^_\7\60\2\2_$\3\2\2\2`a\7`\2\2a&\3\2\2\2bf\7\f\2")
        buf.write("\2cd\7\17\2\2df\7\f\2\2eb\3\2\2\2ec\3\2\2\2f(\3\2\2\2")
        buf.write("gi\t\5\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2kl\3")
        buf.write("\2\2\2lm\b\25\2\2m*\3\2\2\2\13\2/\63\67>DFej\3\b\2\2")
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
    NEWLINE = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'='", 
            "'.'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "VARIABLE", "LITERAL", "LPAREN", "RPAREN", "PLUS", "MINUS", 
            "TIMES", "DIV", "GT", "LT", "EQ", "POINT", "POW", "NEWLINE", 
            "WS" ]

    ruleNames = [ "VARIABLE", "VALID_ID_START", "VALID_ID_CHAR", "LITERAL", 
                  "NUMBER", "E", "SIGN", "LPAREN", "RPAREN", "PLUS", "MINUS", 
                  "TIMES", "DIV", "GT", "LT", "EQ", "POINT", "POW", "NEWLINE", 
                  "WS" ]

    grammarFileName = "Basis.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


