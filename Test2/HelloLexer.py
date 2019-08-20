# Generated from Hello.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\64\n\b\3")
        buf.write("\t\3\t\6\t8\n\t\r\t\16\t9\3\n\3\n\6\n>\n\n\r\n\16\n?\3")
        buf.write("\n\5\nC\n\n\3\13\3\13\6\13G\n\13\r\13\16\13H\3\f\3\f\3")
        buf.write("\r\6\rN\n\r\r\r\16\rO\3\16\6\16S\n\16\r\16\16\16T\3\16")
        buf.write("\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\3\2\b\4\2C\\c|\5\2\62;C\\c|\3\2")
        buf.write("c|\6\2&&C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2^\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35")
        buf.write("\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13&\3\2\2")
        buf.write("\2\r(\3\2\2\2\17\63\3\2\2\2\21\65\3\2\2\2\23;\3\2\2\2")
        buf.write("\25D\3\2\2\2\27J\3\2\2\2\31M\3\2\2\2\33R\3\2\2\2\35\36")
        buf.write("\7*\2\2\36\4\3\2\2\2\37 \7+\2\2 \6\3\2\2\2!\"\7]\2\2\"")
        buf.write("\b\3\2\2\2#$\7/\2\2$%\7@\2\2%\n\3\2\2\2&\'\7_\2\2\'\f")
        buf.write("\3\2\2\2()\7.\2\2)\16\3\2\2\2*+\7v\2\2+,\7t\2\2,-\7w\2")
        buf.write("\2-\64\7g\2\2./\7h\2\2/\60\7c\2\2\60\61\7n\2\2\61\62\7")
        buf.write("u\2\2\62\64\7g\2\2\63*\3\2\2\2\63.\3\2\2\2\64\20\3\2\2")
        buf.write("\2\65\67\7/\2\2\668\t\2\2\2\67\66\3\2\2\289\3\2\2\29\67")
        buf.write("\3\2\2\29:\3\2\2\2:\22\3\2\2\2;=\t\2\2\2<>\t\3\2\2=<\3")
        buf.write("\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3\2\2\2AC\7.\2")
        buf.write("\2BA\3\2\2\2BC\3\2\2\2C\24\3\2\2\2DF\t\4\2\2EG\t\5\2\2")
        buf.write("FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\26\3\2\2\2J")
        buf.write("K\t\4\2\2K\30\3\2\2\2LN\t\6\2\2ML\3\2\2\2NO\3\2\2\2OM")
        buf.write("\3\2\2\2OP\3\2\2\2P\32\3\2\2\2QS\t\7\2\2RQ\3\2\2\2ST\3")
        buf.write("\2\2\2TR\3\2\2\2TU\3\2\2\2UV\3\2\2\2VW\b\16\2\2W\34\3")
        buf.write("\2\2\2\n\2\639?BHOT\3\b\2\2")
        return buf.getvalue()


class HelloLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    Bool = 7
    ActionName = 8
    Value = 9
    Tuplename = 10
    Tupleletter = 11
    ID = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "'->'", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "Bool", "ActionName", "Value", "Tuplename", "Tupleletter", "ID", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "Bool", 
                  "ActionName", "Value", "Tuplename", "Tupleletter", "ID", 
                  "WS" ]

    grammarFileName = "Hello.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


