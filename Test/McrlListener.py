# Generated from Mcrl.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .McrlParser import McrlParser
else:
    from McrlParser import McrlParser
import xml.etree.cElementTree as ET
import os
# This class defines a complete listener for a parse tree produced by McrlParser.
class McrlListener(ParseTreeListener):
    global listaction
    listaction=[]
    global actiondict
    actiondict={}
    # Enter a parse tree produced by McrlParser#mcrl.
    def enterMcrl(self, ctx:McrlParser.McrlContext):
        
        pass

    # Exit a parse tree produced by McrlParser#mcrl.
    def exitMcrl(self, ctx:McrlParser.McrlContext):
        pass


    # Enter a parse tree produced by McrlParser#specification.
    def enterSpecification(self, ctx:McrlParser.SpecificationContext):
        pass

    # Exit a parse tree produced by McrlParser#specification.
    def exitSpecification(self, ctx:McrlParser.SpecificationContext):
        pass


    # Enter a parse tree produced by McrlParser#bullshit.
    def enterBullshit(self, ctx:McrlParser.BullshitContext):
        pass

    # Exit a parse tree produced by McrlParser#bullshit.
    def exitBullshit(self, ctx:McrlParser.BullshitContext):
        pass


    # Enter a parse tree produced by McrlParser#actspec.
    def enterActspec(self, ctx:McrlParser.ActspecContext):
        print("entering act Spec")  
        global actiondict
        
        for element in ctx.actiondef():
            listparam=[]
            listaction=[]
            if element.actiontype() != None:
                for ele in element.actiontype():
                    if ele.getText()[-1] == "#":
                        listparam.append(ele.getText()[0:-1])
                    else:
                        listparam.append(ele.getText())
            if element.actiontype() != None:
                for ele in element.actiondec():
                    if ele.getText()[-1] == "," or ele.getText()[-1]== ":":
                        stringtoadd=ele.getText()[0:-1]
                        listaction.append(stringtoadd)
                    else:
                        listaction.append(ele.getText())
            for action in listaction:
                actiondict[action]=listparam  
        for element in actiondict.keys():
            print(element,actiondict[element])
        pass

    # Exit a parse tree produced by McrlParser#actspec.
    def exitActspec(self, ctx:McrlParser.ActspecContext):
        print("yoy")
        global actiondict
        dicta = ET.Element("dicta")
        for action in actiondict.keys():
            Action=ET.SubElement(dicta,"Action",Value=action)
            for type in actiondict[action]:
                    type=ET.SubElement(Action,"Type",Value=type)
            
                        
        # ET.SubElement(doc, "field1", name="blah").text = "some value1"
        # ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
        
        tree = ET.ElementTree(dicta)
        os.remove("dict.xml")
        tree.write("dict.xml")        
        pass


    # Enter a parse tree produced by McrlParser#actiondef.
    def enterActiondef(self, ctx:McrlParser.ActiondefContext):
        
        pass

    # Exit a parse tree produced by McrlParser#actiondef.
    def exitActiondef(self, ctx:McrlParser.ActiondefContext):
        pass


    # Enter a parse tree produced by McrlParser#actiondec.
    def enterActiondec(self, ctx:McrlParser.ActiondecContext):
        pass

    # Exit a parse tree produced by McrlParser#actiondec.
    def exitActiondec(self, ctx:McrlParser.ActiondecContext):
        pass


    # Enter a parse tree produced by McrlParser#actiontype.
    def enterActiontype(self, ctx:McrlParser.ActiontypeContext):
        pass

    # Exit a parse tree produced by McrlParser#actiontype.
    def exitActiontype(self, ctx:McrlParser.ActiontypeContext):
        pass


    # Enter a parse tree produced by McrlParser#unterminatedStringLiteral.
    def enterUnterminatedStringLiteral(self, ctx:McrlParser.UnterminatedStringLiteralContext):
        pass

    # Exit a parse tree produced by McrlParser#unterminatedStringLiteral.
    def exitUnterminatedStringLiteral(self, ctx:McrlParser.UnterminatedStringLiteralContext):
        pass


