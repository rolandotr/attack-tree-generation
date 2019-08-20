# Generated from Mcrl.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("P\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4\3")
        buf.write("\5\6\5\35\n\5\r\5\16\5\36\3\5\5\5\"\n\5\3\6\6\6%\n\6\r")
        buf.write("\6\16\6&\3\6\7\6*\n\6\f\6\16\6-\13\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7\66\n\7\3\b\6\b9\n\b\r\b\16\b:\3\b\3\b\5")
        buf.write("\b?\n\b\3\t\7\tB\n\t\f\t\16\tE\13\t\3\t\3\t\7\tI\n\t\f")
        buf.write("\t\16\tL\13\t\5\tN\n\t\3\t\4CJ\2\n\2\4\6\b\n\f\16\20\2")
        buf.write("\2\2S\2\22\3\2\2\2\4\24\3\2\2\2\6\31\3\2\2\2\b\34\3\2")
        buf.write("\2\2\n$\3\2\2\2\f\65\3\2\2\2\16>\3\2\2\2\20M\3\2\2\2\22")
        buf.write("\23\5\4\3\2\23\3\3\2\2\2\24\25\5\6\4\2\25\27\5\b\5\2\26")
        buf.write("\30\5\6\4\2\27\26\3\2\2\2\27\30\3\2\2\2\30\5\3\2\2\2\31")
        buf.write("\32\5\20\t\2\32\7\3\2\2\2\33\35\5\n\6\2\34\33\3\2\2\2")
        buf.write("\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37!\3\2\2\2")
        buf.write(" \"\7\b\2\2! \3\2\2\2!\"\3\2\2\2\"\t\3\2\2\2#%\5\f\7\2")
        buf.write("$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'+\3\2\2\2(")
        buf.write("*\5\16\b\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3")
        buf.write("\2\2\2-+\3\2\2\2./\7\3\2\2/\13\3\2\2\2\60\61\7\t\2\2\61")
        buf.write("\66\7\4\2\2\62\63\7\t\2\2\63\66\7\5\2\2\64\66\7\t\2\2")
        buf.write("\65\60\3\2\2\2\65\62\3\2\2\2\65\64\3\2\2\2\66\r\3\2\2")
        buf.write("\2\679\7\t\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2")
        buf.write("\2;<\3\2\2\2<?\7\6\2\2=?\7\t\2\2>8\3\2\2\2>=\3\2\2\2?")
        buf.write("\17\3\2\2\2@B\13\2\2\2A@\3\2\2\2BE\3\2\2\2CD\3\2\2\2C")
        buf.write("A\3\2\2\2DF\3\2\2\2EC\3\2\2\2FN\7\7\2\2GI\13\2\2\2HG\3")
        buf.write("\2\2\2IL\3\2\2\2JK\3\2\2\2JH\3\2\2\2KN\3\2\2\2LJ\3\2\2")
        buf.write("\2MC\3\2\2\2MJ\3\2\2\2N\21\3\2\2\2\r\27\36!&+\65:>CJM")
        return buf.getvalue()


class McrlParser ( Parser ):

    grammarFileName = "Mcrl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "':'", "'#'", "'act'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Acttoken", "Endstring", "Name", "WS", 
                      "OTHER" ]

    RULE_mcrl = 0
    RULE_specification = 1
    RULE_bullshit = 2
    RULE_actspec = 3
    RULE_actiondef = 4
    RULE_actiondec = 5
    RULE_actiontype = 6
    RULE_unterminatedStringLiteral = 7

    ruleNames =  [ "mcrl", "specification", "bullshit", "actspec", "actiondef", 
                   "actiondec", "actiontype", "unterminatedStringLiteral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    Acttoken=5
    Endstring=6
    Name=7
    WS=8
    OTHER=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class McrlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specification(self):
            return self.getTypedRuleContext(McrlParser.SpecificationContext,0)


        def getRuleIndex(self):
            return McrlParser.RULE_mcrl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMcrl" ):
                listener.enterMcrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMcrl" ):
                listener.exitMcrl(self)




    def mcrl(self):

        localctx = McrlParser.McrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_mcrl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.specification()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecificationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bullshit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McrlParser.BullshitContext)
            else:
                return self.getTypedRuleContext(McrlParser.BullshitContext,i)


        def actspec(self):
            return self.getTypedRuleContext(McrlParser.ActspecContext,0)


        def getRuleIndex(self):
            return McrlParser.RULE_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecification" ):
                listener.enterSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecification" ):
                listener.exitSpecification(self)




    def specification(self):

        localctx = McrlParser.SpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.bullshit()
            self.state = 19
            self.actspec()
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 20
                self.bullshit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BullshitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unterminatedStringLiteral(self):
            return self.getTypedRuleContext(McrlParser.UnterminatedStringLiteralContext,0)


        def getRuleIndex(self):
            return McrlParser.RULE_bullshit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBullshit" ):
                listener.enterBullshit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBullshit" ):
                listener.exitBullshit(self)




    def bullshit(self):

        localctx = McrlParser.BullshitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bullshit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.unterminatedStringLiteral()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActspecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actiondef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McrlParser.ActiondefContext)
            else:
                return self.getTypedRuleContext(McrlParser.ActiondefContext,i)


        def Endstring(self):
            return self.getToken(McrlParser.Endstring, 0)

        def getRuleIndex(self):
            return McrlParser.RULE_actspec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActspec" ):
                listener.enterActspec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActspec" ):
                listener.exitActspec(self)




    def actspec(self):

        localctx = McrlParser.ActspecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_actspec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 25
                    self.actiondef()

                else:
                    raise NoViableAltException(self)
                self.state = 28 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 30
                self.match(McrlParser.Endstring)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActiondefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actiondec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McrlParser.ActiondecContext)
            else:
                return self.getTypedRuleContext(McrlParser.ActiondecContext,i)


        def actiontype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McrlParser.ActiontypeContext)
            else:
                return self.getTypedRuleContext(McrlParser.ActiontypeContext,i)


        def getRuleIndex(self):
            return McrlParser.RULE_actiondef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActiondef" ):
                listener.enterActiondef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActiondef" ):
                listener.exitActiondef(self)




    def actiondef(self):

        localctx = McrlParser.ActiondefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_actiondef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 33
                    self.actiondec()

                else:
                    raise NoViableAltException(self)
                self.state = 36 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==McrlParser.Name:
                self.state = 38
                self.actiontype()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(McrlParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActiondecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(McrlParser.Name, 0)

        def getRuleIndex(self):
            return McrlParser.RULE_actiondec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActiondec" ):
                listener.enterActiondec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActiondec" ):
                listener.exitActiondec(self)




    def actiondec(self):

        localctx = McrlParser.ActiondecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_actiondec)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(McrlParser.Name)
                self.state = 47
                self.match(McrlParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(McrlParser.Name)
                self.state = 49
                self.match(McrlParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(McrlParser.Name)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActiontypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(McrlParser.Name)
            else:
                return self.getToken(McrlParser.Name, i)

        def getRuleIndex(self):
            return McrlParser.RULE_actiontype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActiontype" ):
                listener.enterActiontype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActiontype" ):
                listener.exitActiontype(self)




    def actiontype(self):

        localctx = McrlParser.ActiontypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_actiontype)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 53
                    self.match(McrlParser.Name)
                    self.state = 56 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==McrlParser.Name):
                        break

                self.state = 58
                self.match(McrlParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(McrlParser.Name)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnterminatedStringLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Acttoken(self):
            return self.getToken(McrlParser.Acttoken, 0)

        def getRuleIndex(self):
            return McrlParser.RULE_unterminatedStringLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnterminatedStringLiteral" ):
                listener.enterUnterminatedStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnterminatedStringLiteral" ):
                listener.exitUnterminatedStringLiteral(self)




    def unterminatedStringLiteral(self):

        localctx = McrlParser.UnterminatedStringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_unterminatedStringLiteral)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 62
                        self.matchWildcard() 
                    self.state = 67
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 68
                self.match(McrlParser.Acttoken)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 69
                        self.matchWildcard() 
                    self.state = 74
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





