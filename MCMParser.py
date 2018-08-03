# Generated from MCMParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\5\2\25\n\2\6\2\27\n\2\r\2\16\2\30")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\7\5*\n\5\f\5\16\5-\13\5\3\6\3\6\3\6\7\6\62\n\6")
        buf.write("\f\6\16\6\65\13\6\3\7\3\7\3\7\5\7:\n\7\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\tO\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\tZ\n\t\f\t\16\t]\13\t\3\t\2\3\20\n\2\4\6\b\n\f\16\20")
        buf.write("\2\4\3\2\24\25\3\2\26\27\2e\2\26\3\2\2\2\4\32\3\2\2\2")
        buf.write("\6\"\3\2\2\2\b&\3\2\2\2\n.\3\2\2\2\f9\3\2\2\2\16;\3\2")
        buf.write("\2\2\20N\3\2\2\2\22\24\5\4\3\2\23\25\7\5\2\2\24\23\3\2")
        buf.write("\2\2\24\25\3\2\2\2\25\27\3\2\2\2\26\22\3\2\2\2\27\30\3")
        buf.write("\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\3\3\2\2\2\32\33")
        buf.write("\7\4\2\2\33\34\7\6\2\2\34\35\7\7\2\2\35\36\5\6\4\2\36")
        buf.write("\37\7\f\2\2\37 \5\16\b\2 !\7\34\2\2!\5\3\2\2\2\"#\5\b")
        buf.write("\5\2#$\7\13\2\2$%\5\n\6\2%\7\3\2\2\2&+\5\f\7\2\'(\7\n")
        buf.write("\2\2(*\5\f\7\2)\'\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2")
        buf.write("\2,\t\3\2\2\2-+\3\2\2\2.\63\5\f\7\2/\60\7\n\2\2\60\62")
        buf.write("\5\f\7\2\61/\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64")
        buf.write("\3\2\2\2\64\13\3\2\2\2\65\63\3\2\2\2\66:\7\b\2\2\678\7")
        buf.write("\t\2\28:\7\b\2\29\66\3\2\2\29\67\3\2\2\2:\r\3\2\2\2;<")
        buf.write("\5\20\t\2<\17\3\2\2\2=>\b\t\1\2>?\7\31\2\2?@\5\20\t\2")
        buf.write("@A\7\32\2\2AO\3\2\2\2BC\7\27\2\2CO\5\20\t\tDO\7\22\2\2")
        buf.write("EO\7\16\2\2FO\7\17\2\2GO\7\20\2\2HO\7\33\2\2IJ\7\30\2")
        buf.write("\2JK\7\31\2\2KL\5\20\t\2LM\7\32\2\2MO\3\2\2\2N=\3\2\2")
        buf.write("\2NB\3\2\2\2ND\3\2\2\2NE\3\2\2\2NF\3\2\2\2NG\3\2\2\2N")
        buf.write("H\3\2\2\2NI\3\2\2\2O[\3\2\2\2PQ\f\f\2\2QR\7\23\2\2RZ\5")
        buf.write("\20\t\fST\f\13\2\2TU\t\2\2\2UZ\5\20\t\fVW\f\n\2\2WX\t")
        buf.write("\3\2\2XZ\5\20\t\13YP\3\2\2\2YS\3\2\2\2YV\3\2\2\2Z]\3\2")
        buf.write("\2\2[Y\3\2\2\2[\\\3\2\2\2\\\21\3\2\2\2][\3\2\2\2\n\24")
        buf.write("\30+\639NY[")
        return buf.getvalue()


class MCMParser ( Parser ):

    grammarFileName = "MCMParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'{'", "<INVALID>", "<INVALID>", 
                     "'}'", "<INVALID>", "<INVALID>", "<INVALID>", "'='", 
                     "':'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'**'", "'*'", "'/'", "<INVALID>", 
                     "'-'", "'EXP'", "'('", "')'", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "WS", "LPARA", "NEWLINE", "IND", "RPARA", 
                      "CHEM", "STOI", "CHEMPLUS", "EQUAL", "COLON", "WSEQN", 
                      "DOUBLE", "FLOAT", "INT", "WSRATE", "JVEC", "POW", 
                      "MULT", "DIV", "PLUS", "MINUS", "EXP", "LP", "RP", 
                      "VAR", "SEMICOLON" ]

    RULE_reactions = 0
    RULE_reaction = 1
    RULE_eqn = 2
    RULE_reactants = 3
    RULE_products = 4
    RULE_chemitem = 5
    RULE_rate = 6
    RULE_rate_expr = 7

    ruleNames =  [ "reactions", "reaction", "eqn", "reactants", "products", 
                   "chemitem", "rate", "rate_expr" ]

    EOF = Token.EOF
    WS=1
    LPARA=2
    NEWLINE=3
    IND=4
    RPARA=5
    CHEM=6
    STOI=7
    CHEMPLUS=8
    EQUAL=9
    COLON=10
    WSEQN=11
    DOUBLE=12
    FLOAT=13
    INT=14
    WSRATE=15
    JVEC=16
    POW=17
    MULT=18
    DIV=19
    PLUS=20
    MINUS=21
    EXP=22
    LP=23
    RP=24
    VAR=25
    SEMICOLON=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ReactionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reaction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCMParser.ReactionContext)
            else:
                return self.getTypedRuleContext(MCMParser.ReactionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MCMParser.NEWLINE)
            else:
                return self.getToken(MCMParser.NEWLINE, i)

        def getRuleIndex(self):
            return MCMParser.RULE_reactions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReactions" ):
                listener.enterReactions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReactions" ):
                listener.exitReactions(self)




    def reactions(self):

        localctx = MCMParser.ReactionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_reactions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.reaction()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MCMParser.NEWLINE:
                    self.state = 17
                    self.match(MCMParser.NEWLINE)


                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MCMParser.LPARA):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReactionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPARA(self):
            return self.getToken(MCMParser.LPARA, 0)

        def IND(self):
            return self.getToken(MCMParser.IND, 0)

        def RPARA(self):
            return self.getToken(MCMParser.RPARA, 0)

        def eqn(self):
            return self.getTypedRuleContext(MCMParser.EqnContext,0)


        def COLON(self):
            return self.getToken(MCMParser.COLON, 0)

        def rate(self):
            return self.getTypedRuleContext(MCMParser.RateContext,0)


        def SEMICOLON(self):
            return self.getToken(MCMParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MCMParser.RULE_reaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReaction" ):
                listener.enterReaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReaction" ):
                listener.exitReaction(self)




    def reaction(self):

        localctx = MCMParser.ReactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_reaction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(MCMParser.LPARA)
            self.state = 25
            self.match(MCMParser.IND)
            self.state = 26
            self.match(MCMParser.RPARA)
            self.state = 27
            self.eqn()
            self.state = 28
            self.match(MCMParser.COLON)
            self.state = 29
            self.rate()
            self.state = 30
            self.match(MCMParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EqnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reactants(self):
            return self.getTypedRuleContext(MCMParser.ReactantsContext,0)


        def EQUAL(self):
            return self.getToken(MCMParser.EQUAL, 0)

        def products(self):
            return self.getTypedRuleContext(MCMParser.ProductsContext,0)


        def getRuleIndex(self):
            return MCMParser.RULE_eqn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqn" ):
                listener.enterEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqn" ):
                listener.exitEqn(self)




    def eqn(self):

        localctx = MCMParser.EqnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_eqn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.reactants()
            self.state = 33
            self.match(MCMParser.EQUAL)
            self.state = 34
            self.products()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReactantsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chemitem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCMParser.ChemitemContext)
            else:
                return self.getTypedRuleContext(MCMParser.ChemitemContext,i)


        def CHEMPLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MCMParser.CHEMPLUS)
            else:
                return self.getToken(MCMParser.CHEMPLUS, i)

        def getRuleIndex(self):
            return MCMParser.RULE_reactants

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReactants" ):
                listener.enterReactants(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReactants" ):
                listener.exitReactants(self)




    def reactants(self):

        localctx = MCMParser.ReactantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_reactants)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.chemitem()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCMParser.CHEMPLUS:
                self.state = 37
                self.match(MCMParser.CHEMPLUS)
                self.state = 38
                self.chemitem()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProductsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chemitem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCMParser.ChemitemContext)
            else:
                return self.getTypedRuleContext(MCMParser.ChemitemContext,i)


        def CHEMPLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MCMParser.CHEMPLUS)
            else:
                return self.getToken(MCMParser.CHEMPLUS, i)

        def getRuleIndex(self):
            return MCMParser.RULE_products

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProducts" ):
                listener.enterProducts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProducts" ):
                listener.exitProducts(self)




    def products(self):

        localctx = MCMParser.ProductsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_products)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.chemitem()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCMParser.CHEMPLUS:
                self.state = 45
                self.match(MCMParser.CHEMPLUS)
                self.state = 46
                self.chemitem()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ChemitemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MCMParser.RULE_chemitem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ChemContext(ChemitemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MCMParser.ChemitemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHEM(self):
            return self.getToken(MCMParser.CHEM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChem" ):
                listener.enterChem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChem" ):
                listener.exitChem(self)


    class StoiChemContext(ChemitemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MCMParser.ChemitemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STOI(self):
            return self.getToken(MCMParser.STOI, 0)
        def CHEM(self):
            return self.getToken(MCMParser.CHEM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoiChem" ):
                listener.enterStoiChem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoiChem" ):
                listener.exitStoiChem(self)



    def chemitem(self):

        localctx = MCMParser.ChemitemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_chemitem)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCMParser.CHEM]:
                localctx = MCMParser.ChemContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(MCMParser.CHEM)
                pass
            elif token in [MCMParser.STOI]:
                localctx = MCMParser.StoiChemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(MCMParser.STOI)
                self.state = 54
                self.match(MCMParser.CHEM)
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

    class RateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rate_expr(self):
            return self.getTypedRuleContext(MCMParser.Rate_exprContext,0)


        def getRuleIndex(self):
            return MCMParser.RULE_rate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRate" ):
                listener.enterRate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRate" ):
                listener.exitRate(self)




    def rate(self):

        localctx = MCMParser.RateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.rate_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Rate_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def LP(self):
            return self.getToken(MCMParser.LP, 0)

        def rate_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCMParser.Rate_exprContext)
            else:
                return self.getTypedRuleContext(MCMParser.Rate_exprContext,i)


        def RP(self):
            return self.getToken(MCMParser.RP, 0)

        def MINUS(self):
            return self.getToken(MCMParser.MINUS, 0)

        def JVEC(self):
            return self.getToken(MCMParser.JVEC, 0)

        def DOUBLE(self):
            return self.getToken(MCMParser.DOUBLE, 0)

        def FLOAT(self):
            return self.getToken(MCMParser.FLOAT, 0)

        def INT(self):
            return self.getToken(MCMParser.INT, 0)

        def VAR(self):
            return self.getToken(MCMParser.VAR, 0)

        def EXP(self):
            return self.getToken(MCMParser.EXP, 0)

        def POW(self):
            return self.getToken(MCMParser.POW, 0)

        def MULT(self):
            return self.getToken(MCMParser.MULT, 0)

        def DIV(self):
            return self.getToken(MCMParser.DIV, 0)

        def PLUS(self):
            return self.getToken(MCMParser.PLUS, 0)

        def getRuleIndex(self):
            return MCMParser.RULE_rate_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRate_expr" ):
                listener.enterRate_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRate_expr" ):
                listener.exitRate_expr(self)



    def rate_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCMParser.Rate_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_rate_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCMParser.LP]:
                self.state = 60
                self.match(MCMParser.LP)
                self.state = 61
                self.rate_expr(0)
                self.state = 62
                self.match(MCMParser.RP)
                pass
            elif token in [MCMParser.MINUS]:
                self.state = 64
                self.match(MCMParser.MINUS)
                self.state = 65
                self.rate_expr(7)
                pass
            elif token in [MCMParser.JVEC]:
                self.state = 66
                self.match(MCMParser.JVEC)
                pass
            elif token in [MCMParser.DOUBLE]:
                self.state = 67
                self.match(MCMParser.DOUBLE)
                pass
            elif token in [MCMParser.FLOAT]:
                self.state = 68
                self.match(MCMParser.FLOAT)
                pass
            elif token in [MCMParser.INT]:
                self.state = 69
                self.match(MCMParser.INT)
                pass
            elif token in [MCMParser.VAR]:
                self.state = 70
                self.match(MCMParser.VAR)
                pass
            elif token in [MCMParser.EXP]:
                self.state = 71
                self.match(MCMParser.EXP)
                self.state = 72
                self.match(MCMParser.LP)
                self.state = 73
                self.rate_expr(0)
                self.state = 74
                self.match(MCMParser.RP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MCMParser.Rate_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rate_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 79
                        self.match(MCMParser.POW)
                        self.state = 80
                        self.rate_expr(10)
                        pass

                    elif la_ == 2:
                        localctx = MCMParser.Rate_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rate_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 82
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MCMParser.MULT or _la==MCMParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 83
                        self.rate_expr(10)
                        pass

                    elif la_ == 3:
                        localctx = MCMParser.Rate_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rate_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 85
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MCMParser.PLUS or _la==MCMParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 86
                        self.rate_expr(9)
                        pass

             
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.rate_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def rate_expr_sempred(self, localctx:Rate_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




