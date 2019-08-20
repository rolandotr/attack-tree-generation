# Generated from Mcrl.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7=\n\7\3\b\3\b\6\bA\n\b\r\b\16\b")
        buf.write("B\3\t\6\tF\n\t\r\t\16\tG\3\t\3\t\3\n\3\n\3\n\3\n\2\2\13")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\5\4\2C\\")
        buf.write("c|\5\2\62;C\\c|\5\2\13\f\17\17\"\"\2V\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2")
        buf.write("\2\5\27\3\2\2\2\7\31\3\2\2\2\t\33\3\2\2\2\13\35\3\2\2")
        buf.write("\2\r<\3\2\2\2\17>\3\2\2\2\21E\3\2\2\2\23K\3\2\2\2\25\26")
        buf.write("\7=\2\2\26\4\3\2\2\2\27\30\7.\2\2\30\6\3\2\2\2\31\32\7")
        buf.write("<\2\2\32\b\3\2\2\2\33\34\7%\2\2\34\n\3\2\2\2\35\36\7c")
        buf.write("\2\2\36\37\7e\2\2\37 \7v\2\2 \f\3\2\2\2!\"\7u\2\2\"#\7")
        buf.write("q\2\2#$\7t\2\2$=\7v\2\2%&\7o\2\2&\'\7c\2\2\'=\7r\2\2(")
        buf.write(")\7x\2\2)*\7c\2\2*=\7t\2\2+,\7g\2\2,-\7s\2\2-=\7p\2\2")
        buf.write("./\7r\2\2/\60\7t\2\2\60\61\7q\2\2\61=\7e\2\2\62\63\7k")
        buf.write("\2\2\63\64\7p\2\2\64\65\7k\2\2\65=\7v\2\2\66\67\7>\2\2")
        buf.write("\678\7G\2\289\7Q\2\29:\7H\2\2:;\3\2\2\2;=\7@\2\2<!\3\2")
        buf.write("\2\2<%\3\2\2\2<(\3\2\2\2<+\3\2\2\2<.\3\2\2\2<\62\3\2\2")
        buf.write("\2<\66\3\2\2\2=\16\3\2\2\2>@\t\2\2\2?A\t\3\2\2@?\3\2\2")
        buf.write("\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\20\3\2\2\2DF\t\4\2\2")
        buf.write("ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\b")
        buf.write("\t\2\2J\22\3\2\2\2KL\13\2\2\2LM\3\2\2\2MN\b\n\2\2N\24")
        buf.write("\3\2\2\2\6\2<BG\3\b\2\2")
        return buf.getvalue()


class McrlLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    Acttoken = 5
    Endstring = 6
    Name = 7
    WS = 8
    OTHER = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "':'", "'#'", "'act'" ]

    symbolicNames = [ "<INVALID>",
            "Acttoken", "Endstring", "Name", "WS", "OTHER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "Acttoken", "Endstring", 
                  "Name", "WS", "OTHER" ]

    grammarFileName = "Mcrl.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


