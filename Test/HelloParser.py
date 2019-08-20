# Generated from Hello.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\3\3\3\6\3\32")
        buf.write("\n\3\r\3\16\3\33\3\4\3\4\3\5\3\5\5\5\"\n\5\3\6\3\6\6\6")
        buf.write("&\n\6\r\6\16\6\'\3\6\3\6\3\7\3\7\6\7.\n\7\r\7\16\7/\3")
        buf.write("\7\3\7\5\7\64\n\7\3\7\5\7\67\n\7\5\79\n\7\3\b\3\b\3\b")
        buf.write("\3\b\6\b?\n\b\r\b\16\b@\3\b\3\b\3\b\3\b\3\b\5\bH\n\b\3")
        buf.write("\t\3\t\3\t\6\tM\n\t\r\t\16\tN\3\t\3\t\3\t\3\t\5\tU\n\t")
        buf.write("\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2Z\2\23\3\2\2\2\4\27")
        buf.write("\3\2\2\2\6\35\3\2\2\2\b\37\3\2\2\2\n#\3\2\2\2\f8\3\2\2")
        buf.write("\2\16:\3\2\2\2\20T\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2")
        buf.write("\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\3\3\2\2")
        buf.write("\2\27\31\5\6\4\2\30\32\5\b\5\2\31\30\3\2\2\2\32\33\3\2")
        buf.write("\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\5\3\2\2\2\35\36\7")
        buf.write("\16\2\2\36\7\3\2\2\2\37!\5\n\6\2 \"\5\20\t\2! \3\2\2\2")
        buf.write("!\"\3\2\2\2\"\t\3\2\2\2#%\7\3\2\2$&\5\f\7\2%$\3\2\2\2")
        buf.write("&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\7\4\2\2")
        buf.write("*\13\3\2\2\2+-\7\f\2\2,.\5\16\b\2-,\3\2\2\2./\3\2\2\2")
        buf.write("/-\3\2\2\2/\60\3\2\2\2\609\3\2\2\2\61\63\7\f\2\2\62\64")
        buf.write("\7\5\2\2\63\62\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65")
        buf.write("\67\7\4\2\2\66\65\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28+")
        buf.write("\3\2\2\28\61\3\2\2\29\r\3\2\2\2:;\7\6\2\2;<\7\r\2\2<>")
        buf.write("\7\3\2\2=?\7\13\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3")
        buf.write("\2\2\2AB\3\2\2\2BC\7\4\2\2CD\7\7\2\2DE\7\t\2\2EG\7\b\2")
        buf.write("\2FH\7\5\2\2GF\3\2\2\2GH\3\2\2\2H\17\3\2\2\2IJ\7\n\2\2")
        buf.write("JL\7\3\2\2KM\7\13\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO")
        buf.write("\3\2\2\2OP\3\2\2\2PQ\7\4\2\2QU\7\7\2\2RS\7\n\2\2SU\7\7")
        buf.write("\2\2TI\3\2\2\2TR\3\2\2\2U\21\3\2\2\2\16\25\33!\'/\63\66")
        buf.write("8@GNT")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'['", "'->'", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Bool", "ActionName", 
                      "Value", "Tuplename", "Tupleletter", "ID", "WS" ]

    RULE_r = 0
    RULE_traces = 1
    RULE_traceid = 2
    RULE_trace = 3
    RULE_status = 4
    RULE_tupleallDecl = 5
    RULE_tupledecl = 6
    RULE_trans = 7

    ruleNames =  [ "r", "traces", "traceid", "trace", "status", "tupleallDecl", 
                   "tupledecl", "trans" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    Bool=7
    ActionName=8
    Value=9
    Tuplename=10
    Tupleletter=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def traces(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.TracesContext)
            else:
                return self.getTypedRuleContext(HelloParser.TracesContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)




    def r(self):

        localctx = HelloParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.traces()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HelloParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TracesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def traceid(self):
            return self.getTypedRuleContext(HelloParser.TraceidContext,0)


        def trace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.TraceContext)
            else:
                return self.getTypedRuleContext(HelloParser.TraceContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_traces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTraces" ):
                listener.enterTraces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTraces" ):
                listener.exitTraces(self)




    def traces(self):

        localctx = HelloParser.TracesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_traces)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.traceid()
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.trace()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HelloParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TraceidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_traceid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTraceid" ):
                listener.enterTraceid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTraceid" ):
                listener.exitTraceid(self)




    def traceid(self):

        localctx = HelloParser.TraceidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_traceid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(HelloParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TraceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def status(self):
            return self.getTypedRuleContext(HelloParser.StatusContext,0)


        def trans(self):
            return self.getTypedRuleContext(HelloParser.TransContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_trace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrace" ):
                listener.enterTrace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrace" ):
                listener.exitTrace(self)




    def trace(self):

        localctx = HelloParser.TraceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_trace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.status()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HelloParser.ActionName:
                self.state = 30
                self.trans()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tupleallDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.TupleallDeclContext)
            else:
                return self.getTypedRuleContext(HelloParser.TupleallDeclContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_status

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatus" ):
                listener.enterStatus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatus" ):
                listener.exitStatus(self)




    def status(self):

        localctx = HelloParser.StatusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_status)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(HelloParser.T__0)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.tupleallDecl()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HelloParser.Tuplename):
                    break

            self.state = 39
            self.match(HelloParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleallDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Tuplename(self):
            return self.getToken(HelloParser.Tuplename, 0)

        def tupledecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.TupledeclContext)
            else:
                return self.getTypedRuleContext(HelloParser.TupledeclContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_tupleallDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleallDecl" ):
                listener.enterTupleallDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleallDecl" ):
                listener.exitTupleallDecl(self)




    def tupleallDecl(self):

        localctx = HelloParser.TupleallDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tupleallDecl)
        self._la = 0 # Token type
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(HelloParser.Tuplename)
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 42
                    self.tupledecl()
                    self.state = 45 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==HelloParser.T__3):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(HelloParser.Tuplename)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HelloParser.T__2:
                    self.state = 48
                    self.match(HelloParser.T__2)


                self.state = 52
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 51
                    self.match(HelloParser.T__1)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupledeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Tupleletter(self):
            return self.getToken(HelloParser.Tupleletter, 0)

        def Bool(self):
            return self.getToken(HelloParser.Bool, 0)

        def Value(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.Value)
            else:
                return self.getToken(HelloParser.Value, i)

        def getRuleIndex(self):
            return HelloParser.RULE_tupledecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupledecl" ):
                listener.enterTupledecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupledecl" ):
                listener.exitTupledecl(self)




    def tupledecl(self):

        localctx = HelloParser.TupledeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tupledecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(HelloParser.T__3)
            self.state = 57
            self.match(HelloParser.Tupleletter)
            self.state = 58
            self.match(HelloParser.T__0)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.match(HelloParser.Value)
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HelloParser.Value):
                    break

            self.state = 64
            self.match(HelloParser.T__1)
            self.state = 65
            self.match(HelloParser.T__4)
            self.state = 66
            self.match(HelloParser.Bool)
            self.state = 67
            self.match(HelloParser.T__5)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HelloParser.T__2:
                self.state = 68
                self.match(HelloParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ActionName(self):
            return self.getToken(HelloParser.ActionName, 0)

        def Value(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.Value)
            else:
                return self.getToken(HelloParser.Value, i)

        def getRuleIndex(self):
            return HelloParser.RULE_trans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrans" ):
                listener.enterTrans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrans" ):
                listener.exitTrans(self)




    def trans(self):

        localctx = HelloParser.TransContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_trans)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(HelloParser.ActionName)
                self.state = 72
                self.match(HelloParser.T__0)
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 73
                    self.match(HelloParser.Value)
                    self.state = 76 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==HelloParser.Value):
                        break

                self.state = 78
                self.match(HelloParser.T__1)
                self.state = 79
                self.match(HelloParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(HelloParser.ActionName)
                self.state = 81
                self.match(HelloParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





