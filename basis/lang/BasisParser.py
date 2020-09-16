# Generated from basis/grammar/Basis.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("\u0177\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\3\2\7\2I\n\2")
        buf.write("\f\2\16\2L\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3[\n\3\3\4\3\4\3\4\3\4\5\4a\n\4\6\4c")
        buf.write("\n\4\r\4\16\4d\3\4\3\4\3\5\3\5\3\5\3\5\5\5m\n\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6x\n\6\f\6\16\6{\13\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0083\n\7\f\7\16\7\u0086")
        buf.write("\13\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u008e\n\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u0095\n\b\3\t\3\t\3\t\3\t\5\t\u009b\n\t")
        buf.write("\3\n\3\n\3\n\5\n\u00a0\n\n\3\13\3\13\5\13\u00a4\n\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\5\f\u00ac\n\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00b2\n\f\3\f\3\f\5\f\u00b6\n\f\3\r\3\r\3\r\5\r")
        buf.write("\u00bb\n\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c3\n\r\f\r\16")
        buf.write("\r\u00c6\13\r\3\16\3\16\3\16\3\16\3\16\5\16\u00cd\n\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00e3")
        buf.write("\n\17\3\20\3\20\3\20\6\20\u00e8\n\20\r\20\16\20\u00e9")
        buf.write("\5\20\u00ec\n\20\3\21\3\21\3\21\7\21\u00f1\n\21\f\21\16")
        buf.write("\21\u00f4\13\21\3\22\3\22\3\22\7\22\u00f9\n\22\f\22\16")
        buf.write("\22\u00fc\13\22\3\23\3\23\3\23\7\23\u0101\n\23\f\23\16")
        buf.write("\23\u0104\13\23\3\23\5\23\u0107\n\23\3\24\3\24\3\24\7")
        buf.write("\24\u010c\n\24\f\24\16\24\u010f\13\24\3\24\5\24\u0112")
        buf.write("\n\24\3\25\3\25\3\25\5\25\u0117\n\25\3\26\3\26\3\26\7")
        buf.write("\26\u011c\n\26\f\26\16\26\u011f\13\26\3\27\3\27\3\27\7")
        buf.write("\27\u0124\n\27\f\27\16\27\u0127\13\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u012e\n\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0137\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u013e")
        buf.write("\n\32\3\33\3\33\7\33\u0142\n\33\f\33\16\33\u0145\13\33")
        buf.write("\3\34\3\34\5\34\u0149\n\34\3\34\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u0150\n\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0158")
        buf.write("\n\35\3\36\3\36\3\37\3\37\3 \3 \3 \5 \u0161\n \3!\3!\3")
        buf.write("!\3!\3!\5!\u0168\n!\3\"\3\"\3\"\3\"\7\"\u016e\n\"\f\"")
        buf.write("\16\"\u0171\13\"\3\"\3\"\3#\3#\3#\2\5\n\f\30$\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BD\2\6\4\2\'\'))\3\2#&\3\2\35\36\3\2\37!\2\u0192\2")
        buf.write("J\3\2\2\2\4Z\3\2\2\2\6\\\3\2\2\2\bh\3\2\2\2\nq\3\2\2\2")
        buf.write("\f|\3\2\2\2\16\u0094\3\2\2\2\20\u009a\3\2\2\2\22\u009c")
        buf.write("\3\2\2\2\24\u00a1\3\2\2\2\26\u00a8\3\2\2\2\30\u00ba\3")
        buf.write("\2\2\2\32\u00cc\3\2\2\2\34\u00e2\3\2\2\2\36\u00eb\3\2")
        buf.write("\2\2 \u00ed\3\2\2\2\"\u00f5\3\2\2\2$\u0106\3\2\2\2&\u0111")
        buf.write("\3\2\2\2(\u0116\3\2\2\2*\u0118\3\2\2\2,\u0120\3\2\2\2")
        buf.write(".\u012d\3\2\2\2\60\u0136\3\2\2\2\62\u013d\3\2\2\2\64\u013f")
        buf.write("\3\2\2\2\66\u014f\3\2\2\28\u0157\3\2\2\2:\u0159\3\2\2")
        buf.write("\2<\u015b\3\2\2\2>\u0160\3\2\2\2@\u0167\3\2\2\2B\u0169")
        buf.write("\3\2\2\2D\u0174\3\2\2\2FI\7/\2\2GI\5\4\3\2HF\3\2\2\2H")
        buf.write("G\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2KM\3\2\2\2LJ\3")
        buf.write("\2\2\2MN\7\2\2\3N\3\3\2\2\2O[\5*\26\2P[\5 \21\2Q[\5\32")
        buf.write("\16\2R[\5\16\b\2S[\5\26\f\2T[\5\22\n\2U[\5\24\13\2V[\5")
        buf.write("\b\5\2W[\5> \2X[\5:\36\2Y[\5<\37\2ZO\3\2\2\2ZP\3\2\2\2")
        buf.write("ZQ\3\2\2\2ZR\3\2\2\2ZS\3\2\2\2ZT\3\2\2\2ZU\3\2\2\2ZV\3")
        buf.write("\2\2\2ZW\3\2\2\2ZX\3\2\2\2ZY\3\2\2\2[\5\3\2\2\2\\]\7/")
        buf.write("\2\2]b\7\61\2\2^`\5\4\3\2_a\7/\2\2`_\3\2\2\2`a\3\2\2\2")
        buf.write("ac\3\2\2\2b^\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2ef\3")
        buf.write("\2\2\2fg\7\62\2\2g\7\3\2\2\2hi\7\3\2\2ij\5D#\2jl\7\24")
        buf.write("\2\2km\5\n\6\2lk\3\2\2\2lm\3\2\2\2mn\3\2\2\2no\7\25\2")
        buf.write("\2op\5\6\4\2p\t\3\2\2\2qr\b\6\1\2rs\5D#\2sy\3\2\2\2tu")
        buf.write("\f\3\2\2uv\7\4\2\2vx\5D#\2wt\3\2\2\2x{\3\2\2\2yw\3\2\2")
        buf.write("\2yz\3\2\2\2z\13\3\2\2\2{y\3\2\2\2|}\b\7\1\2}~\5 \21\2")
        buf.write("~\u0084\3\2\2\2\177\u0080\f\3\2\2\u0080\u0081\7\4\2\2")
        buf.write("\u0081\u0083\5 \21\2\u0082\177\3\2\2\2\u0083\u0086\3\2")
        buf.write("\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\r\3")
        buf.write("\2\2\2\u0086\u0084\3\2\2\2\u0087\u0088\7\5\2\2\u0088\u0095")
        buf.write("\5 \21\2\u0089\u008a\7\5\2\2\u008a\u008b\5 \21\2\u008b")
        buf.write("\u008d\5\6\4\2\u008c\u008e\5\20\t\2\u008d\u008c\3\2\2")
        buf.write("\2\u008d\u008e\3\2\2\2\u008e\u0095\3\2\2\2\u008f\u0090")
        buf.write("\7\5\2\2\u0090\u0091\5 \21\2\u0091\u0092\7/\2\2\u0092")
        buf.write("\u0093\5\20\t\2\u0093\u0095\3\2\2\2\u0094\u0087\3\2\2")
        buf.write("\2\u0094\u0089\3\2\2\2\u0094\u008f\3\2\2\2\u0095\17\3")
        buf.write("\2\2\2\u0096\u0097\7\6\2\2\u0097\u009b\5\16\b\2\u0098")
        buf.write("\u0099\7\6\2\2\u0099\u009b\5\6\4\2\u009a\u0096\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009b\21\3\2\2\2\u009c\u009d\7\7")
        buf.write("\2\2\u009d\u009f\5 \21\2\u009e\u00a0\5\6\4\2\u009f\u009e")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\23\3\2\2\2\u00a1\u00a3")
        buf.write("\7\b\2\2\u00a2\u00a4\5\6\4\2\u00a3\u00a2\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\7\7\2\2")
        buf.write("\u00a6\u00a7\5 \21\2\u00a7\25\3\2\2\2\u00a8\u00a9\7\t")
        buf.write("\2\2\u00a9\u00ab\7\24\2\2\u00aa\u00ac\5\30\r\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00ae\7\n\2\2\u00ae\u00af\5 \21\2\u00af\u00b1\7\n\2\2")
        buf.write("\u00b0\u00b2\5\30\r\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b5\7\25\2\2\u00b4")
        buf.write("\u00b6\5\6\4\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\27\3\2\2\2\u00b7\u00b8\b\r\1\2\u00b8\u00bb\5\32")
        buf.write("\16\2\u00b9\u00bb\5 \21\2\u00ba\u00b7\3\2\2\2\u00ba\u00b9")
        buf.write("\3\2\2\2\u00bb\u00c4\3\2\2\2\u00bc\u00bd\f\4\2\2\u00bd")
        buf.write("\u00be\7\4\2\2\u00be\u00c3\5\32\16\2\u00bf\u00c0\f\3\2")
        buf.write("\2\u00c0\u00c1\7\4\2\2\u00c1\u00c3\5 \21\2\u00c2\u00bc")
        buf.write("\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\31\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c8\5\36\20\2\u00c8\u00c9\7(\2")
        buf.write("\2\u00c9\u00ca\5 \21\2\u00ca\u00cd\3\2\2\2\u00cb\u00cd")
        buf.write("\5\34\17\2\u00cc\u00c7\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\33\3\2\2\2\u00ce\u00cf\5\36\20\2\u00cf\u00d0\7\30\2\2")
        buf.write("\u00d0\u00d1\5 \21\2\u00d1\u00e3\3\2\2\2\u00d2\u00d3\5")
        buf.write("\36\20\2\u00d3\u00d4\7\31\2\2\u00d4\u00d5\5 \21\2\u00d5")
        buf.write("\u00e3\3\2\2\2\u00d6\u00d7\5\36\20\2\u00d7\u00d8\7\32")
        buf.write("\2\2\u00d8\u00d9\5 \21\2\u00d9\u00e3\3\2\2\2\u00da\u00db")
        buf.write("\5\36\20\2\u00db\u00dc\7\33\2\2\u00dc\u00dd\5 \21\2\u00dd")
        buf.write("\u00e3\3\2\2\2\u00de\u00df\5\36\20\2\u00df\u00e0\7\34")
        buf.write("\2\2\u00e0\u00e1\5 \21\2\u00e1\u00e3\3\2\2\2\u00e2\u00ce")
        buf.write("\3\2\2\2\u00e2\u00d2\3\2\2\2\u00e2\u00d6\3\2\2\2\u00e2")
        buf.write("\u00da\3\2\2\2\u00e2\u00de\3\2\2\2\u00e3\35\3\2\2\2\u00e4")
        buf.write("\u00ec\5D#\2\u00e5\u00e7\58\35\2\u00e6\u00e8\5\66\34\2")
        buf.write("\u00e7\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7\3")
        buf.write("\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00e4")
        buf.write("\3\2\2\2\u00eb\u00e5\3\2\2\2\u00ec\37\3\2\2\2\u00ed\u00f2")
        buf.write("\5\"\22\2\u00ee\u00ef\7+\2\2\u00ef\u00f1\5\"\22\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2")
        buf.write("\u00f2\u00f3\3\2\2\2\u00f3!\3\2\2\2\u00f4\u00f2\3\2\2")
        buf.write("\2\u00f5\u00fa\5$\23\2\u00f6\u00f7\7*\2\2\u00f7\u00f9")
        buf.write("\5$\23\2\u00f8\u00f6\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb#\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u0102\5&\24\2\u00fe\u00ff\t\2\2\2")
        buf.write("\u00ff\u0101\5&\24\2\u0100\u00fe\3\2\2\2\u0101\u0104\3")
        buf.write("\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0107")
        buf.write("\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0107\5&\24\2\u0106")
        buf.write("\u00fd\3\2\2\2\u0106\u0105\3\2\2\2\u0107%\3\2\2\2\u0108")
        buf.write("\u010d\5(\25\2\u0109\u010a\t\3\2\2\u010a\u010c\5(\25\2")
        buf.write("\u010b\u0109\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3")
        buf.write("\2\2\2\u010d\u010e\3\2\2\2\u010e\u0112\3\2\2\2\u010f\u010d")
        buf.write("\3\2\2\2\u0110\u0112\5(\25\2\u0111\u0108\3\2\2\2\u0111")
        buf.write("\u0110\3\2\2\2\u0112\'\3\2\2\2\u0113\u0114\7\"\2\2\u0114")
        buf.write("\u0117\5(\25\2\u0115\u0117\5*\26\2\u0116\u0113\3\2\2\2")
        buf.write("\u0116\u0115\3\2\2\2\u0117)\3\2\2\2\u0118\u011d\5,\27")
        buf.write("\2\u0119\u011a\t\4\2\2\u011a\u011c\5,\27\2\u011b\u0119")
        buf.write("\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e+\3\2\2\2\u011f\u011d\3\2\2\2\u0120")
        buf.write("\u0125\5.\30\2\u0121\u0122\t\5\2\2\u0122\u0124\5.\30\2")
        buf.write("\u0123\u0121\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3")
        buf.write("\2\2\2\u0125\u0126\3\2\2\2\u0126-\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0128\u0129\7\35\2\2\u0129\u012e\5.\30\2\u012a")
        buf.write("\u012b\7\36\2\2\u012b\u012e\5.\30\2\u012c\u012e\5\60\31")
        buf.write("\2\u012d\u0128\3\2\2\2\u012d\u012a\3\2\2\2\u012d\u012c")
        buf.write("\3\2\2\2\u012e/\3\2\2\2\u012f\u0130\5D#\2\u0130\u0131")
        buf.write("\7\26\2\2\u0131\u0137\3\2\2\2\u0132\u0133\5D#\2\u0133")
        buf.write("\u0134\7\27\2\2\u0134\u0137\3\2\2\2\u0135\u0137\5\62\32")
        buf.write("\2\u0136\u012f\3\2\2\2\u0136\u0132\3\2\2\2\u0136\u0135")
        buf.write("\3\2\2\2\u0137\61\3\2\2\2\u0138\u0139\7\27\2\2\u0139\u013e")
        buf.write("\5D#\2\u013a\u013b\7\26\2\2\u013b\u013e\5D#\2\u013c\u013e")
        buf.write("\5\64\33\2\u013d\u0138\3\2\2\2\u013d\u013a\3\2\2\2\u013d")
        buf.write("\u013c\3\2\2\2\u013e\63\3\2\2\2\u013f\u0143\58\35\2\u0140")
        buf.write("\u0142\5\66\34\2\u0141\u0140\3\2\2\2\u0142\u0145\3\2\2")
        buf.write("\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\65\3")
        buf.write("\2\2\2\u0145\u0143\3\2\2\2\u0146\u0148\7\24\2\2\u0147")
        buf.write("\u0149\5\f\7\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u0150\7\25\2\2\u014b\u014c")
        buf.write("\7\13\2\2\u014c\u014d\5*\26\2\u014d\u014e\7\f\2\2\u014e")
        buf.write("\u0150\3\2\2\2\u014f\u0146\3\2\2\2\u014f\u014b\3\2\2\2")
        buf.write("\u0150\67\3\2\2\2\u0151\u0158\5@!\2\u0152\u0158\5D#\2")
        buf.write("\u0153\u0154\7\24\2\2\u0154\u0155\5 \21\2\u0155\u0156")
        buf.write("\7\25\2\2\u0156\u0158\3\2\2\2\u0157\u0151\3\2\2\2\u0157")
        buf.write("\u0152\3\2\2\2\u0157\u0153\3\2\2\2\u01589\3\2\2\2\u0159")
        buf.write("\u015a\7\21\2\2\u015a;\3\2\2\2\u015b\u015c\7\22\2\2\u015c")
        buf.write("=\3\2\2\2\u015d\u015e\7\23\2\2\u015e\u0161\5 \21\2\u015f")
        buf.write("\u0161\7\23\2\2\u0160\u015d\3\2\2\2\u0160\u015f\3\2\2")
        buf.write("\2\u0161?\3\2\2\2\u0162\u0168\7\17\2\2\u0163\u0168\7\r")
        buf.write("\2\2\u0164\u0168\7\16\2\2\u0165\u0168\7\20\2\2\u0166\u0168")
        buf.write("\5B\"\2\u0167\u0162\3\2\2\2\u0167\u0163\3\2\2\2\u0167")
        buf.write("\u0164\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0166\3\2\2\2")
        buf.write("\u0168A\3\2\2\2\u0169\u016a\7\13\2\2\u016a\u016f\5 \21")
        buf.write("\2\u016b\u016c\7\4\2\2\u016c\u016e\5 \21\2\u016d\u016b")
        buf.write("\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u0172\3\2\2\2\u0171\u016f\3\2\2\2")
        buf.write("\u0172\u0173\7\f\2\2\u0173C\3\2\2\2\u0174\u0175\7-\2\2")
        buf.write("\u0175E\3\2\2\2,HJZ`dly\u0084\u008d\u0094\u009a\u009f")
        buf.write("\u00a3\u00ab\u00b1\u00b5\u00ba\u00c2\u00c4\u00cc\u00e2")
        buf.write("\u00e9\u00eb\u00f2\u00fa\u0102\u0106\u010d\u0111\u0116")
        buf.write("\u011d\u0125\u012d\u0136\u013d\u0143\u0148\u014f\u0157")
        buf.write("\u0160\u0167\u016f")
        return buf.getvalue()


class BasisParser ( Parser ):

    grammarFileName = "Basis.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "','", "'if'", "'else'", 
                     "'while'", "'do'", "'for'", "';'", "'['", "']'", "<INVALID>", 
                     "'null'", "<INVALID>", "<INVALID>", "'break'", "'continue'", 
                     "'return'", "'('", "')'", "'++'", "'--'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'>'", "'<'", "'>='", "'<='", "'=='", 
                     "'='", "'!='", "'&&'", "'||'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BOOL", "NULL", 
                      "NUMBER", "STRING", "BREAK", "CONTINUE", "RETURN", 
                      "LPAREN", "RPAREN", "INCREMENT", "DECREMENT", "IADD", 
                      "ISUB", "IMUL", "IDIV", "IMOD", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "NOT", "GT", "LT", "GET", "LET", "DUBEQ", 
                      "EQ", "NEQ", "AND", "OR", "POINT", "VARIABLE", "COMMENT", 
                      "NEWLINE", "WS", "INDENT", "DEDENT" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_function_definition = 3
    RULE_parameter_list = 4
    RULE_argument_list = 5
    RULE_if_statement = 6
    RULE_else_statement = 7
    RULE_while_statement = 8
    RULE_do_while_statement = 9
    RULE_for_statement = 10
    RULE_for_expression = 11
    RULE_assignment = 12
    RULE_inline_assignment = 13
    RULE_l_value = 14
    RULE_comparison = 15
    RULE_and_comparison = 16
    RULE_eq_comparison = 17
    RULE_then_comparison = 18
    RULE_not_comparison = 19
    RULE_expression = 20
    RULE_term = 21
    RULE_signedAtom = 22
    RULE_postcrement_expression = 23
    RULE_precrement_expression = 24
    RULE_atom_expression = 25
    RULE_trailer = 26
    RULE_atom = 27
    RULE_break_ = 28
    RULE_continue_ = 29
    RULE_return_ = 30
    RULE_literal = 31
    RULE_array_literal = 32
    RULE_variable = 33

    ruleNames =  [ "start", "statement", "block", "function_definition", 
                   "parameter_list", "argument_list", "if_statement", "else_statement", 
                   "while_statement", "do_while_statement", "for_statement", 
                   "for_expression", "assignment", "inline_assignment", 
                   "l_value", "comparison", "and_comparison", "eq_comparison", 
                   "then_comparison", "not_comparison", "expression", "term", 
                   "signedAtom", "postcrement_expression", "precrement_expression", 
                   "atom_expression", "trailer", "atom", "break_", "continue_", 
                   "return_", "literal", "array_literal", "variable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    BOOL=11
    NULL=12
    NUMBER=13
    STRING=14
    BREAK=15
    CONTINUE=16
    RETURN=17
    LPAREN=18
    RPAREN=19
    INCREMENT=20
    DECREMENT=21
    IADD=22
    ISUB=23
    IMUL=24
    IDIV=25
    IMOD=26
    ADD=27
    SUB=28
    MUL=29
    DIV=30
    MOD=31
    NOT=32
    GT=33
    LT=34
    GET=35
    LET=36
    DUBEQ=37
    EQ=38
    NEQ=39
    AND=40
    OR=41
    POINT=42
    VARIABLE=43
    COMMENT=44
    NEWLINE=45
    WS=46
    INDENT=47
    DEDENT=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BasisParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.NEWLINE)
            else:
                return self.getToken(BasisParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasisParser.StatementContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasisParser.T__0) | (1 << BasisParser.T__2) | (1 << BasisParser.T__4) | (1 << BasisParser.T__5) | (1 << BasisParser.T__6) | (1 << BasisParser.T__8) | (1 << BasisParser.BOOL) | (1 << BasisParser.NULL) | (1 << BasisParser.NUMBER) | (1 << BasisParser.STRING) | (1 << BasisParser.BREAK) | (1 << BasisParser.CONTINUE) | (1 << BasisParser.RETURN) | (1 << BasisParser.LPAREN) | (1 << BasisParser.INCREMENT) | (1 << BasisParser.DECREMENT) | (1 << BasisParser.ADD) | (1 << BasisParser.SUB) | (1 << BasisParser.NOT) | (1 << BasisParser.VARIABLE) | (1 << BasisParser.NEWLINE))) != 0):
                self.state = 70
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BasisParser.NEWLINE]:
                    self.state = 68
                    self.match(BasisParser.NEWLINE)
                    pass
                elif token in [BasisParser.T__0, BasisParser.T__2, BasisParser.T__4, BasisParser.T__5, BasisParser.T__6, BasisParser.T__8, BasisParser.BOOL, BasisParser.NULL, BasisParser.NUMBER, BasisParser.STRING, BasisParser.BREAK, BasisParser.CONTINUE, BasisParser.RETURN, BasisParser.LPAREN, BasisParser.INCREMENT, BasisParser.DECREMENT, BasisParser.ADD, BasisParser.SUB, BasisParser.NOT, BasisParser.VARIABLE]:
                    self.state = 69
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(BasisParser.EOF)
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


        def if_statement(self):
            return self.getTypedRuleContext(BasisParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BasisParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(BasisParser.While_statementContext,0)


        def do_while_statement(self):
            return self.getTypedRuleContext(BasisParser.Do_while_statementContext,0)


        def function_definition(self):
            return self.getTypedRuleContext(BasisParser.Function_definitionContext,0)


        def return_(self):
            return self.getTypedRuleContext(BasisParser.Return_Context,0)


        def break_(self):
            return self.getTypedRuleContext(BasisParser.Break_Context,0)


        def continue_(self):
            return self.getTypedRuleContext(BasisParser.Continue_Context,0)


        def getRuleIndex(self):
            return BasisParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BasisParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.comparison()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.while_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 83
                self.do_while_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 84
                self.function_definition()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 85
                self.return_()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 86
                self.break_()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 87
                self.continue_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.NEWLINE)
            else:
                return self.getToken(BasisParser.NEWLINE, i)

        def INDENT(self):
            return self.getToken(BasisParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(BasisParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasisParser.StatementContext,i)


        def getRuleIndex(self):
            return BasisParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = BasisParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(BasisParser.NEWLINE)
            self.state = 91
            self.match(BasisParser.INDENT)
            self.state = 96 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self.statement()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BasisParser.NEWLINE:
                    self.state = 93
                    self.match(BasisParser.NEWLINE)


                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasisParser.T__0) | (1 << BasisParser.T__2) | (1 << BasisParser.T__4) | (1 << BasisParser.T__5) | (1 << BasisParser.T__6) | (1 << BasisParser.T__8) | (1 << BasisParser.BOOL) | (1 << BasisParser.NULL) | (1 << BasisParser.NUMBER) | (1 << BasisParser.STRING) | (1 << BasisParser.BREAK) | (1 << BasisParser.CONTINUE) | (1 << BasisParser.RETURN) | (1 << BasisParser.LPAREN) | (1 << BasisParser.INCREMENT) | (1 << BasisParser.DECREMENT) | (1 << BasisParser.ADD) | (1 << BasisParser.SUB) | (1 << BasisParser.NOT) | (1 << BasisParser.VARIABLE))) != 0)):
                    break

            self.state = 100
            self.match(BasisParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BasisParser.VariableContext,0)


        def LPAREN(self):
            return self.getToken(BasisParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BasisParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(BasisParser.BlockContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(BasisParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_function_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = BasisParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BasisParser.T__0)
            self.state = 103
            self.variable()
            self.state = 104
            self.match(BasisParser.LPAREN)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasisParser.VARIABLE:
                self.state = 105
                self.parameter_list(0)


            self.state = 108
            self.match(BasisParser.RPAREN)
            self.state = 109
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BasisParser.VariableContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(BasisParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)



    def parameter_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BasisParser.Parameter_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_parameter_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.variable()
            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BasisParser.Parameter_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parameter_list)
                    self.state = 114
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 115
                    self.match(BasisParser.T__1)
                    self.state = 116
                    self.variable() 
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def argument_list(self):
            return self.getTypedRuleContext(BasisParser.Argument_listContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)



    def argument_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BasisParser.Argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.comparison()
            self._ctx.stop = self._input.LT(-1)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BasisParser.Argument_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 125
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 126
                    self.match(BasisParser.T__1)
                    self.state = 127
                    self.comparison() 
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def block(self):
            return self.getTypedRuleContext(BasisParser.BlockContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(BasisParser.Else_statementContext,0)


        def NEWLINE(self):
            return self.getToken(BasisParser.NEWLINE, 0)

        def getRuleIndex(self):
            return BasisParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BasisParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(BasisParser.T__2)
                self.state = 134
                self.comparison()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(BasisParser.T__2)
                self.state = 136
                self.comparison()
                self.state = 137
                self.block()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BasisParser.T__3:
                    self.state = 138
                    self.else_statement()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(BasisParser.T__2)
                self.state = 142
                self.comparison()
                self.state = 143
                self.match(BasisParser.NEWLINE)
                self.state = 144
                self.else_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(BasisParser.If_statementContext,0)


        def block(self):
            return self.getTypedRuleContext(BasisParser.BlockContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = BasisParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_else_statement)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(BasisParser.T__3)
                self.state = 149
                self.if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(BasisParser.T__3)
                self.state = 151
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def block(self):
            return self.getTypedRuleContext(BasisParser.BlockContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = BasisParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(BasisParser.T__4)
            self.state = 155
            self.comparison()
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 156
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def block(self):
            return self.getTypedRuleContext(BasisParser.BlockContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_do_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_statement" ):
                return visitor.visitDo_while_statement(self)
            else:
                return visitor.visitChildren(self)




    def do_while_statement(self):

        localctx = BasisParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_do_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(BasisParser.T__5)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasisParser.NEWLINE:
                self.state = 160
                self.block()


            self.state = 163
            self.match(BasisParser.T__4)
            self.state = 164
            self.comparison()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BasisParser.LPAREN, 0)

        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def RPAREN(self):
            return self.getToken(BasisParser.RPAREN, 0)

        def for_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.For_expressionContext)
            else:
                return self.getTypedRuleContext(BasisParser.For_expressionContext,i)


        def block(self):
            return self.getTypedRuleContext(BasisParser.BlockContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BasisParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(BasisParser.T__6)
            self.state = 167
            self.match(BasisParser.LPAREN)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasisParser.T__8) | (1 << BasisParser.BOOL) | (1 << BasisParser.NULL) | (1 << BasisParser.NUMBER) | (1 << BasisParser.STRING) | (1 << BasisParser.LPAREN) | (1 << BasisParser.INCREMENT) | (1 << BasisParser.DECREMENT) | (1 << BasisParser.ADD) | (1 << BasisParser.SUB) | (1 << BasisParser.NOT) | (1 << BasisParser.VARIABLE))) != 0):
                self.state = 168
                self.for_expression(0)


            self.state = 171
            self.match(BasisParser.T__7)
            self.state = 172
            self.comparison()
            self.state = 173
            self.match(BasisParser.T__7)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasisParser.T__8) | (1 << BasisParser.BOOL) | (1 << BasisParser.NULL) | (1 << BasisParser.NUMBER) | (1 << BasisParser.STRING) | (1 << BasisParser.LPAREN) | (1 << BasisParser.INCREMENT) | (1 << BasisParser.DECREMENT) | (1 << BasisParser.ADD) | (1 << BasisParser.SUB) | (1 << BasisParser.NOT) | (1 << BasisParser.VARIABLE))) != 0):
                self.state = 174
                self.for_expression(0)


            self.state = 177
            self.match(BasisParser.RPAREN)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 178
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(BasisParser.AssignmentContext,0)


        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def for_expression(self):
            return self.getTypedRuleContext(BasisParser.For_expressionContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_for_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_expression" ):
                return visitor.visitFor_expression(self)
            else:
                return visitor.visitChildren(self)



    def for_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BasisParser.For_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_for_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 182
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 183
                self.comparison()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 192
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = BasisParser.For_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_for_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 187
                        self.match(BasisParser.T__1)
                        self.state = 188
                        self.assignment()
                        pass

                    elif la_ == 2:
                        localctx = BasisParser.For_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_for_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 190
                        self.match(BasisParser.T__1)
                        self.state = 191
                        self.comparison()
                        pass

             
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def l_value(self):
            return self.getTypedRuleContext(BasisParser.L_valueContext,0)


        def EQ(self):
            return self.getToken(BasisParser.EQ, 0)

        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def inline_assignment(self):
            return self.getTypedRuleContext(BasisParser.Inline_assignmentContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = BasisParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.l_value()
                self.state = 198
                self.match(BasisParser.EQ)
                self.state = 199
                self.comparison()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.inline_assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def l_value(self):
            return self.getTypedRuleContext(BasisParser.L_valueContext,0)


        def IADD(self):
            return self.getToken(BasisParser.IADD, 0)

        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def ISUB(self):
            return self.getToken(BasisParser.ISUB, 0)

        def IMUL(self):
            return self.getToken(BasisParser.IMUL, 0)

        def IDIV(self):
            return self.getToken(BasisParser.IDIV, 0)

        def IMOD(self):
            return self.getToken(BasisParser.IMOD, 0)

        def getRuleIndex(self):
            return BasisParser.RULE_inline_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInline_assignment" ):
                return visitor.visitInline_assignment(self)
            else:
                return visitor.visitChildren(self)




    def inline_assignment(self):

        localctx = BasisParser.Inline_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_inline_assignment)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.l_value()
                self.state = 205
                self.match(BasisParser.IADD)
                self.state = 206
                self.comparison()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.l_value()
                self.state = 209
                self.match(BasisParser.ISUB)
                self.state = 210
                self.comparison()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.l_value()
                self.state = 213
                self.match(BasisParser.IMUL)
                self.state = 214
                self.comparison()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 216
                self.l_value()
                self.state = 217
                self.match(BasisParser.IDIV)
                self.state = 218
                self.comparison()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 220
                self.l_value()
                self.state = 221
                self.match(BasisParser.IMOD)
                self.state = 222
                self.comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class L_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BasisParser.VariableContext,0)


        def atom(self):
            return self.getTypedRuleContext(BasisParser.AtomContext,0)


        def trailer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.TrailerContext)
            else:
                return self.getTypedRuleContext(BasisParser.TrailerContext,i)


        def getRuleIndex(self):
            return BasisParser.RULE_l_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_value" ):
                return visitor.visitL_value(self)
            else:
                return visitor.visitChildren(self)




    def l_value(self):

        localctx = BasisParser.L_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_l_value)
        self._la = 0 # Token type
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.atom()
                self.state = 229 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 228
                    self.trailer()
                    self.state = 231 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BasisParser.T__8 or _la==BasisParser.LPAREN):
                        break

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

        def and_comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.And_comparisonContext)
            else:
                return self.getTypedRuleContext(BasisParser.And_comparisonContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.OR)
            else:
                return self.getToken(BasisParser.OR, i)

        def getRuleIndex(self):
            return BasisParser.RULE_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = BasisParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.and_comparison()
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 236
                    self.match(BasisParser.OR)
                    self.state = 237
                    self.and_comparison() 
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_comparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eq_comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.Eq_comparisonContext)
            else:
                return self.getTypedRuleContext(BasisParser.Eq_comparisonContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.AND)
            else:
                return self.getToken(BasisParser.AND, i)

        def getRuleIndex(self):
            return BasisParser.RULE_and_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_comparison" ):
                return visitor.visitAnd_comparison(self)
            else:
                return visitor.visitChildren(self)




    def and_comparison(self):

        localctx = BasisParser.And_comparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_and_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.eq_comparison()
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 244
                    self.match(BasisParser.AND)
                    self.state = 245
                    self.eq_comparison() 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eq_comparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def then_comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.Then_comparisonContext)
            else:
                return self.getTypedRuleContext(BasisParser.Then_comparisonContext,i)


        def DUBEQ(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.DUBEQ)
            else:
                return self.getToken(BasisParser.DUBEQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.NEQ)
            else:
                return self.getToken(BasisParser.NEQ, i)

        def getRuleIndex(self):
            return BasisParser.RULE_eq_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq_comparison" ):
                return visitor.visitEq_comparison(self)
            else:
                return visitor.visitChildren(self)




    def eq_comparison(self):

        localctx = BasisParser.Eq_comparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_eq_comparison)
        self._la = 0 # Token type
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.then_comparison()
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 252
                        _la = self._input.LA(1)
                        if not(_la==BasisParser.DUBEQ or _la==BasisParser.NEQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 253
                        self.then_comparison() 
                    self.state = 258
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.then_comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Then_comparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.Not_comparisonContext)
            else:
                return self.getTypedRuleContext(BasisParser.Not_comparisonContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.LT)
            else:
                return self.getToken(BasisParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.GT)
            else:
                return self.getToken(BasisParser.GT, i)

        def GET(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.GET)
            else:
                return self.getToken(BasisParser.GET, i)

        def LET(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.LET)
            else:
                return self.getToken(BasisParser.LET, i)

        def getRuleIndex(self):
            return BasisParser.RULE_then_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThen_comparison" ):
                return visitor.visitThen_comparison(self)
            else:
                return visitor.visitChildren(self)




    def then_comparison(self):

        localctx = BasisParser.Then_comparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_then_comparison)
        self._la = 0 # Token type
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.not_comparison()
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 263
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasisParser.GT) | (1 << BasisParser.LT) | (1 << BasisParser.GET) | (1 << BasisParser.LET))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 264
                        self.not_comparison() 
                    self.state = 269
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.not_comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_comparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BasisParser.NOT, 0)

        def not_comparison(self):
            return self.getTypedRuleContext(BasisParser.Not_comparisonContext,0)


        def expression(self):
            return self.getTypedRuleContext(BasisParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_not_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_comparison" ):
                return visitor.visitNot_comparison(self)
            else:
                return visitor.visitChildren(self)




    def not_comparison(self):

        localctx = BasisParser.Not_comparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_not_comparison)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(BasisParser.NOT)
                self.state = 274
                self.not_comparison()
                pass
            elif token in [BasisParser.T__8, BasisParser.BOOL, BasisParser.NULL, BasisParser.NUMBER, BasisParser.STRING, BasisParser.LPAREN, BasisParser.INCREMENT, BasisParser.DECREMENT, BasisParser.ADD, BasisParser.SUB, BasisParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.expression()
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


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.TermContext)
            else:
                return self.getTypedRuleContext(BasisParser.TermContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.ADD)
            else:
                return self.getToken(BasisParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.SUB)
            else:
                return self.getToken(BasisParser.SUB, i)

        def getRuleIndex(self):
            return BasisParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BasisParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.term()
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 279
                    _la = self._input.LA(1)
                    if not(_la==BasisParser.ADD or _la==BasisParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 280
                    self.term() 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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

        def signedAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.SignedAtomContext)
            else:
                return self.getTypedRuleContext(BasisParser.SignedAtomContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.MUL)
            else:
                return self.getToken(BasisParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.DIV)
            else:
                return self.getToken(BasisParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(BasisParser.MOD)
            else:
                return self.getToken(BasisParser.MOD, i)

        def getRuleIndex(self):
            return BasisParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = BasisParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.signedAtom()
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 287
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasisParser.MUL) | (1 << BasisParser.DIV) | (1 << BasisParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.signedAtom() 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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

        def ADD(self):
            return self.getToken(BasisParser.ADD, 0)

        def signedAtom(self):
            return self.getTypedRuleContext(BasisParser.SignedAtomContext,0)


        def SUB(self):
            return self.getToken(BasisParser.SUB, 0)

        def postcrement_expression(self):
            return self.getTypedRuleContext(BasisParser.Postcrement_expressionContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_signedAtom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignedAtom" ):
                return visitor.visitSignedAtom(self)
            else:
                return visitor.visitChildren(self)




    def signedAtom(self):

        localctx = BasisParser.SignedAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_signedAtom)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.ADD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(BasisParser.ADD)
                self.state = 295
                self.signedAtom()
                pass
            elif token in [BasisParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(BasisParser.SUB)
                self.state = 297
                self.signedAtom()
                pass
            elif token in [BasisParser.T__8, BasisParser.BOOL, BasisParser.NULL, BasisParser.NUMBER, BasisParser.STRING, BasisParser.LPAREN, BasisParser.INCREMENT, BasisParser.DECREMENT, BasisParser.VARIABLE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.postcrement_expression()
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


    class Postcrement_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BasisParser.VariableContext,0)


        def INCREMENT(self):
            return self.getToken(BasisParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(BasisParser.DECREMENT, 0)

        def precrement_expression(self):
            return self.getTypedRuleContext(BasisParser.Precrement_expressionContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_postcrement_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostcrement_expression" ):
                return visitor.visitPostcrement_expression(self)
            else:
                return visitor.visitChildren(self)




    def postcrement_expression(self):

        localctx = BasisParser.Postcrement_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_postcrement_expression)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.variable()
                self.state = 302
                self.match(BasisParser.INCREMENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.variable()
                self.state = 305
                self.match(BasisParser.DECREMENT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.precrement_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Precrement_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECREMENT(self):
            return self.getToken(BasisParser.DECREMENT, 0)

        def variable(self):
            return self.getTypedRuleContext(BasisParser.VariableContext,0)


        def INCREMENT(self):
            return self.getToken(BasisParser.INCREMENT, 0)

        def atom_expression(self):
            return self.getTypedRuleContext(BasisParser.Atom_expressionContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_precrement_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecrement_expression" ):
                return visitor.visitPrecrement_expression(self)
            else:
                return visitor.visitChildren(self)




    def precrement_expression(self):

        localctx = BasisParser.Precrement_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_precrement_expression)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.DECREMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(BasisParser.DECREMENT)
                self.state = 311
                self.variable()
                pass
            elif token in [BasisParser.INCREMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(BasisParser.INCREMENT)
                self.state = 313
                self.variable()
                pass
            elif token in [BasisParser.T__8, BasisParser.BOOL, BasisParser.NULL, BasisParser.NUMBER, BasisParser.STRING, BasisParser.LPAREN, BasisParser.VARIABLE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.atom_expression()
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


    class Atom_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(BasisParser.AtomContext,0)


        def trailer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.TrailerContext)
            else:
                return self.getTypedRuleContext(BasisParser.TrailerContext,i)


        def getRuleIndex(self):
            return BasisParser.RULE_atom_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom_expression" ):
                return visitor.visitAtom_expression(self)
            else:
                return visitor.visitChildren(self)




    def atom_expression(self):

        localctx = BasisParser.Atom_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_atom_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.atom()
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 318
                    self.trailer() 
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrailerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BasisParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BasisParser.RPAREN, 0)

        def argument_list(self):
            return self.getTypedRuleContext(BasisParser.Argument_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(BasisParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_trailer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrailer" ):
                return visitor.visitTrailer(self)
            else:
                return visitor.visitChildren(self)




    def trailer(self):

        localctx = BasisParser.TrailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_trailer)
        self._la = 0 # Token type
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(BasisParser.LPAREN)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasisParser.T__8) | (1 << BasisParser.BOOL) | (1 << BasisParser.NULL) | (1 << BasisParser.NUMBER) | (1 << BasisParser.STRING) | (1 << BasisParser.LPAREN) | (1 << BasisParser.INCREMENT) | (1 << BasisParser.DECREMENT) | (1 << BasisParser.ADD) | (1 << BasisParser.SUB) | (1 << BasisParser.NOT) | (1 << BasisParser.VARIABLE))) != 0):
                    self.state = 325
                    self.argument_list(0)


                self.state = 328
                self.match(BasisParser.RPAREN)
                pass
            elif token in [BasisParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.match(BasisParser.T__8)
                self.state = 330
                self.expression()
                self.state = 331
                self.match(BasisParser.T__9)
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

        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


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
        self.enterRule(localctx, 54, self.RULE_atom)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.T__8, BasisParser.BOOL, BasisParser.NULL, BasisParser.NUMBER, BasisParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.literal()
                pass
            elif token in [BasisParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.variable()
                pass
            elif token in [BasisParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
                self.match(BasisParser.LPAREN)
                self.state = 338
                self.comparison()
                self.state = 339
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


    class Break_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BasisParser.BREAK, 0)

        def getRuleIndex(self):
            return BasisParser.RULE_break_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_" ):
                return visitor.visitBreak_(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = BasisParser.Break_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_break_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(BasisParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BasisParser.CONTINUE, 0)

        def getRuleIndex(self):
            return BasisParser.RULE_continue_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_" ):
                return visitor.visitContinue_(self)
            else:
                return visitor.visitChildren(self)




    def continue_(self):

        localctx = BasisParser.Continue_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continue_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(BasisParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BasisParser.RETURN, 0)

        def comparison(self):
            return self.getTypedRuleContext(BasisParser.ComparisonContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_return_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_" ):
                return visitor.visitReturn_(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = BasisParser.Return_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_)
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(BasisParser.RETURN)
                self.state = 348
                self.comparison()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(BasisParser.RETURN)
                pass


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

        def NUMBER(self):
            return self.getToken(BasisParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(BasisParser.BOOL, 0)

        def NULL(self):
            return self.getToken(BasisParser.NULL, 0)

        def STRING(self):
            return self.getToken(BasisParser.STRING, 0)

        def array_literal(self):
            return self.getTypedRuleContext(BasisParser.Array_literalContext,0)


        def getRuleIndex(self):
            return BasisParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BasisParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_literal)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasisParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(BasisParser.NUMBER)
                pass
            elif token in [BasisParser.BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.match(BasisParser.BOOL)
                pass
            elif token in [BasisParser.NULL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.match(BasisParser.NULL)
                pass
            elif token in [BasisParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 355
                self.match(BasisParser.STRING)
                pass
            elif token in [BasisParser.T__8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 356
                self.array_literal()
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


    class Array_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasisParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(BasisParser.ComparisonContext,i)


        def getRuleIndex(self):
            return BasisParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = BasisParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(BasisParser.T__8)
            self.state = 360
            self.comparison()
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasisParser.T__1:
                self.state = 361
                self.match(BasisParser.T__1)
                self.state = 362
                self.comparison()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 368
            self.match(BasisParser.T__9)
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
        self.enterRule(localctx, 66, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(BasisParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.parameter_list_sempred
        self._predicates[5] = self.argument_list_sempred
        self._predicates[11] = self.for_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def parameter_list_sempred(self, localctx:Parameter_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def argument_list_sempred(self, localctx:Argument_listContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def for_expression_sempred(self, localctx:For_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




